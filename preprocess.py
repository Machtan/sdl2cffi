import sys
import os
import re

def clean_function(text):
    if "SDL_PRINTF_FORMAT_STRING" in text:
        return ""
    else:
        return text

def clean_struct(text):
    return text.replace("SDLCALL", "")

_bad_pat = r"\n\s*(SDL_[a-zA-Z0-9_]*)\s*=\s*\("
bad_pat = re.compile(_bad_pat)
def clean_enum(text):
    match = bad_pat.search(text)
    if match:
        print("found bad enum pat in enum: {}".format(text.splitlines()[-1].split(" ")[1][:-1]))
        bad = match.groups()[0]
        split = text.splitlines()
        lines = [line for line in split if not line.startswith(("{", "}", "typedef"))]
        order = []
        values = {}
        for line in lines:
            expr = line.split(",")[0]
            print(line)
            name, val = expr.split("=", 1)
            values[name.strip()] = val.strip()
            order.append(name.strip())
        
        badval = values[bad]
        for name, value in values.items():
            if name in badval:
                badval = badval.replace(name, value)
        
        print("Bad:")
        print(badval)
        values[bad] = eval(badval)
        
        parts = [split[0], split[1]]
        for i, key in enumerate(order):
            if i != len(order)-1:
                comma = ","
            else:
                comma = ""
            text = "    {} = {}{}".format(key, values[key], comma)
            parts.append(text)
        parts.append(split[-1])
        t = os.linesep.join(parts)
        
        print("Converted:")
        print(t)
        return t
    else:
        return text

# NOTE: The order is important... I should fix that, tbh.
pats = [
    #"define": "#define\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+(?:[0-9]+|(?:0x[0-9a-fA-F]+)|(?:[a-zA-Z_][a-zA-Z0-9_]*\s*\\|)|(?:[(]\s*\\\\))",
    ("include", r"#include\s*\"([^\"]+)\""),
    ("typedef", r"typedef\s+([a-zA-Z_][a-zA-Z0-9_]*)((?:\s|[*])+)([a-zA-Z_][a-zA-Z0-9_]*)"),
    ("callback", r"typedef\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+\(([^;]+);"),
    ("empty struct", r"typedef struct ([a-zA-Z_][a-zA-Z0-9_]*)\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;"),
    ("enum", r"typedef enum\s+[{]((?:.|\n)+?)\n[}]\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;"),
    ("struct", r"typedef struct\s*([a-zA-Z_][a-zA-Z0-9_]*)?\s*[{]((?:.|\n)+?)\n[}]\s*([a-zA-Z_][a-zA-Z0-9_]*)?\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*;"),
    ("function", r"extern DECLSPEC\s+(.*?)\s+SDLCALL ([^;]*?);"),
]

patterns = [ (k, re.compile(pat)) for k, pat in pats ] 
_fmt_typedef = "typedef {} {};"
_fmt_callback = "typedef {} ({};"
_fmt_define = "#define {} ..."
_fmt_empty_struct = "typedef struct {} {};"
_fmt_struct = "typedef struct {}\n{{{}\n}} {} {};"
_fmt_enum = "typedef enum\n{{{}\n}} {};"
_fmt_function = "{} {};"
_invalid_typedef_names = {"struct", "enum"}
debug = False
def _process_text(text, output, ignore, include_handler=None, debug_name=None):
    
    filtered = [ (k, v) for k, v in patterns if k not in ignore ]
    items = []
    if debug_name is not None:
        items.append((0, "\n// ========= {!r} =========\n".format(debug_name)))
    
    def add(start, text):
        items.append(start, text)
    
    for pid, pattern in filtered:
        
            
        for match in pattern.finditer(text):
            if pid == "define":
                name = match.groups()[0]
                if debug: print("define: {}".format(name))
                items.append((match.start(), _fmt_define.format(name)))
                
            elif pid == "typedef":
                type_, pad, name = match.groups()
                if type_ not in _invalid_typedef_names:
                    if debug: print("typedef: {} = {}".format(name, type_+pad))
                    items.append((match.start(), _fmt_typedef.format(type_+pad, name)))
            
            elif pid == "callback":
                rettype, body = match.groups()
                print("callback: {!r} ({}".format(rettype, body))
                items.append((match.start(), _fmt_callback.format(rettype, body.replace("SDLCALL", ""))))
            
            elif pid == "empty struct":
                body, name = match.groups()
                if debug: print("empty struct: {}".format(name))
                items.append((match.start(), _fmt_empty_struct.format(body, name)))
            
            elif pid == "struct":
                structname, body, extra, alias = match.groups()
                if debug: print("struct: {}".format(alias))
                # The 'extra' argument is only used SDL_audio.h and to 
                # ensure that the audio is packed correctly with GCC
                # see 'SDL_audio.h:195'
                items.append((match.start(), clean_struct(_fmt_struct.format(structname, body, "", alias))))
            
            elif pid == "enum":
                body, name = match.groups()
                if debug: print("enum: {}".format(name))
                items.append((match.start(), clean_enum(_fmt_enum.format(body, name))))
            
            elif pid == "function":
                rettype, signature = match.groups()
                if debug: print("function: {} -> {}".format(signature, rettype))
                items.append((match.start(), clean_function(_fmt_function.format(rettype, signature))))
            
            elif pid == "include":
                name = match.groups()[0]
                if debug: print("include: {!r}".format(name))
                if include_handler is not None:
                    include_handler(name, output)
    
    items.sort()
    for _, item in items:
        output.append(item)

def _process_file(path, output, ignore, include_handler=None):
    with open(path) as f:
        text = f.read()
    
    _process_text(text, output, ignore, include_handler=include_handler, debug_name=os.path.basename(path))


def process_file(path, ignore_map=None, excluded=None, recursive=False):
    if ignore_map is None:
        ignore_map = dict()
    
    output = []
    basename = os.path.basename(path)
    s = set()
    ignore = ignore_map.get(basename, s)
    
    if recursive:
        abspath = os.path.abspath(path)
        dirname = os.path.dirname(abspath)
        if excluded is None:
            excluded = set()
        excluded.add(abspath)
        def include_handler(name, output):
            p = os.path.join(dirname, name)
            if p in excluded:
                #print("{!r} is already included!".format(name))
                pass
            elif not os.path.exists(p):
                excluded.add(p)
                print("Could not find {!r}!".format(name))
            else:
                print("-> Including {!r}......".format(name))
                excluded.add(p)
                s = set()
                ign = ignore_map.get(name, s)
                _process_file(p, output, ign, include_handler=include_handler)
        
        _process_file(path, output, ignore, include_handler=include_handler)
            
    else:
        _process_file(path, output, ignore)
    
    return os.linesep.join(output)


def main():
    """Entry point"""
    if len(sys.argv) < 2:
        return print("Usage: python3 preprocess.py <file.h>")
    
    
    output = process_file(sys.argv[1], recursive=True)
    
    print("\n//=========== OUTPUT ============\n")
    print(output)
    
if __name__ == '__main__':
    main()
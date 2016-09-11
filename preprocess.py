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

def parse_enum(text):
    split = text.splitlines()
    lines = [line for line in split if not line.startswith(("{", "}", "typedef", "enum"))]
    items = "\n".join(lines).replace("\n", "").split(",")
    order = []
    values = {}
    for line in items:
        print(line)
        if not "=" in line:
            name = line.strip()
            values[name] = None
            order.append(name)
        else:
            name, val = line.split("=", 1)
            values[name.strip()] = val.strip()
            order.append(name.strip())
    
    for name, value in values.items():
        if value is not None and "|" in value:
            for oname, ovalue in values.items():
                if oname in value:
                    value = value.replace(oname, ovalue)
            value = eval(value)
            values[name] = value
    
    return values

_bad_pat = r"\n\s*(SDL_[a-zA-Z0-9_]*)\s*=\s*\("
bad_pat = re.compile(_bad_pat)
def clean_enum(text):
    match = bad_pat.search(text)
    if match:
        print("found bad enum pat in enum: {}".format(text.splitlines()[-1].split(" ")[-1][:-1]))
        print(text)
        
        split = text.splitlines()
        lines = [line for line in split if not line.startswith(("{", "}", "typedef", "enum"))]
        items = "\n".join(lines).replace("\n", "").split(",")
        order = []
        values = {}
        for line in items:
            print(line)
            if not "=" in line:
                name = line.strip()
                values[name] = None
                order.append(name)
            else:
                name, val = line.split("=", 1)
                values[name.strip()] = val.strip()
                order.append(name.strip())
        
        for name, value in values.items():
            if value is not None and "|" in value:
                for oname, ovalue in values.items():
                    if oname in value:
                        value = value.replace(oname, ovalue)
                value = eval(value)
                values[name] = value
        
        
        parts = [split[0], split[1]]
        for i, key in enumerate(order):
            if i != len(order)-1:
                comma = ","
            else:
                comma = ""
            value = values[key]
            if value == None:
                text = "    {}{}".format(key, comma)
            else:
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
    ("typedef", r"typedef\s+([a-zA-Z_][a-zA-Z0-9_]*)((?:\s|[*])+)([a-zA-Z_][a-zA-Z0-9_]*)[^\{]*?;"),
    ("callback", r"typedef\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+\(([^;]+);"),
    ("empty struct", r"typedef struct ([a-zA-Z_][a-zA-Z0-9_]*)\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;"),
    ("typedef enum", r"typedef enum\s+[{]((?:.|\n)+?)\n[}]\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;"),
    ("enum", r"enum\s+[{]((?:.|\n)+?)\n[}]\s*;"),
    ("struct", r"typedef struct\s*([a-zA-Z_][a-zA-Z0-9_]*)?\s*[{]((?:.|\n)+?)\n[}]\s*([a-zA-Z_][a-zA-Z0-9_]*)?\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*;"),
    ("function", r"extern DECLSPEC\s+(.*?)\s+SDLCALL ([^;]*?);"),
]

patterns = [ (k, re.compile(pat)) for k, pat in pats ]
named_patterns = { k: r for k, r in patterns }
_fmt_typedef = "typedef {} {};"
_fmt_callback = "typedef {} ({};"
_fmt_define = "#define {} ..."
_fmt_empty_struct = "typedef struct {} {};"
_fmt_struct = "typedef struct {}\n{{{}\n}} {} {};"
_fmt_typedef_enum = "typedef enum\n{{{}\n}} {};"
_fmt_enum = "enum\n{{{}\n}};"
_fmt_function = "{} {};"
_invalid_typedef_names = {"struct", "enum"}
debug = True
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
            
            elif pid == "typedef enum":
                body, name = match.groups()
                if debug: print("enum: {}".format(name))
                items.append((match.start(), clean_enum(_fmt_typedef_enum.format(body, name))))
            
            elif pid == "enum":
                body = match.groups()[0]
                if debug: print("unnamed enum:")
                items.append((match.start(), clean_enum(_fmt_enum.format(body))))
            
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


def fix_enums(text):
    parts = []
    start = 0
    for match in named_patterns["enum"].finditer(text):
        parts.append(text[start:match.start()])
        enum = match.group(0)
        
        values = parse_enum(enum)
        print("=========== VALUES ==============")
        import pprint
        pprint.pprint(values)
        
        parts.append(clean_enum(enum))
        start = match.end()
    
    parts.append(text[start:])
    text = "".join(parts)
    
    parts.clear()
    start = 0
    for match in named_patterns["typedef enum"].finditer(text):
        parts.append(text[start:match.start()])
        enum = match.group(0)
        parts.append(clean_enum(enum))
        start = match.end()
    
    parts.append(text[start:])
    return "".join(parts)
    

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

def output(text, outfile=None, silent=False):
    if outfile:
        with open(outfile, "w") as f:
            f.write(text)
    else:
        if not silent:
            print(text)

def main():
    """Entry point"""
    import argparse
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("header")
    parser.add_argument("--output", "-o")
    parser.add_argument("--fix-enums", "-f", action="store_true", default=False)
    parser.add_argument("--silent", "-s", action="store_true", default=False)
    
    args = parser.parse_args(sys.argv[1:])
    if args.fix_enums:
        with open(args.header) as f:
            text = f.read()
        fixed = fix_enums(text)
        output(fixed, outfile=args.output, silent=args.silent)
    else:
        cleaned = process_file(args.header, recursive=True)
    
        output("\n//=========== OUTPUT ============\n", outfile=args.output)
        output(cleaned, outfile=args.output, silent=args.silent)


if __name__ == '__main__':
    main()
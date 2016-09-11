import os
import sys
import re
import subprocess

def run_preprocessor(headerfile):
    res = subprocess.run(["cc", "-E", "-P", headerfile], 
        stdout=subprocess.PIPE, universal_newlines=True)
    return res.stdout

RE_TYPEDEF_ENUM = re.compile(r"typedef enum\s+[{]((?:.|\n)+?)\n[}]\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;")
RE_ENUM = re.compile(r"enum\s+[{]([^}]*?)[}]\s*;")
def remove_enums(text):
    for pat in [RE_TYPEDEF_ENUM, RE_ENUM]:
        parts = []
        start = 0
        for match in pat.finditer(text):
            parts.append(text[start : match.start()])
            start = match.end()
        parts.append(text[start :])
        text = "".join(parts)
    return text

GET_PLATFORM = "const char * SDL_GetPlatform (void);"
BOOL_DEF = """\
typedef enum
{
    SDL_FALSE = 0,
    SDL_TRUE = 1
} SDL_bool;\
"""
def remove_non_sdl_parts(text):
    return os.linesep.join([
        GET_PLATFORM,
        BOOL_DEF,
        text.split(BOOL_DEF)[-1],
    ])

def remove_empty_lines(text):
    lines = []
    for line in text.splitlines():
        if line == "" or line.isspace():
            continue
        else:
            lines.append(line)
    return os.linesep.join(lines)

def remove_attributes(text):
    text = text.replace("extern __attribute__ ((visibility(\"default\"))) ", "")
    text = text.replace("__attribute__((always_inline)) ", "")
    text = text.replace("__attribute__((packed)) ", "")
    text = text.replace("__attribute__((analyzer_noreturn))", "")
    return text

def remove_inline_stuff(text):
    lines = []
    i = 0
    split = list(text.splitlines())
    last = len(split)
    while i < len(split):
        line = split[i]
        # Fix both __inline__ and __inline (__m128)
        pat = "static __inline"
        if line.startswith(pat):
            #print("Removing inline: {}".format(line[len(pat):].split("(")[0]))
            if i == last: break
            i += 1
            nextline = split[i]
            if nextline.startswith("{"):
                i += 1
                l = split[i]
                while not l.startswith("}"):
                    i += 1
                    l = split[i]
                i += 1
            else:
                continue
        else:
            lines.append(line)
            i += 1
    
    return os.linesep.join(lines)
            

LINE_REPLACEMENTS = {
    "int SDL_SetError( const char *fmt, ...)": 
        "int SDL_SetError( const char *fmt, ...);",
}
REMOVED_LINES = [
    "typedef int SDL_dummy_",
    "int SDL_sscanf",
    "int SDL_vsscanf",
    "int SDL_snprintf",
    "int SDL_vsnprintf",
    "extern",
]
for line in REMOVED_LINES:
    LINE_REPLACEMENTS[line] = ""

def fix_other_cases(text):
    lines = []
    for line in text.splitlines():
        replaced = False
        for start, rep in LINE_REPLACEMENTS.items():
            if line.startswith(start):
                lines.append(rep)
                replaced = True
        
        if not replaced:        
            lines.append(line)
    
    return os.linesep.join(lines)

def remove_weird_functions(text):
    lines = []
    for line in text.splitlines():
        if "__attribute__" in line and line.endswith(";"):
            lines.append(line.split("__attribute__", 1)[0].rstrip()+";")
        else:
            lines.append(line)
    return os.linesep.join(lines)

RE_ASM = re.compile(r"\n\s*[^\(]+?\([^\)]*\)\n[{](?:.|\n)*?(?:\n[}])")
def remove_asm_functions(text):
    parts = []
    start = 0
    for match in RE_ASM.finditer(text):
        full = match.group(0)
        name = full.split("(", 1)[0].rsplit(" ")[-1]
        #print("Removing asm function: {!r}".format(name))
        #print(full)
        parts.append(text[start : match.start()])
        start = match.end()
        parts.append("")
    
    parts.append(text[start :])
    return "".join(parts)

def remove_functions(text, functions):
    lines = []
    i = 0
    split = list(text.splitlines())
    while i < len(split):
        line = split[i]
        replaced = False
        for function in functions:
            if line.startswith(function):
                print("Replacing {!r}".format(function))
                i += 1
                line = split[i]
                while not line.endswith(");"):
                    i += 1
                    line = split[i]
                i += 1
                replaced = True
                break
        if not replaced:
            lines.append(line)
            i += 1
    
    return os.linesep.join(lines)

def clean_header(text):
    text = remove_non_sdl_parts(text)
    text = remove_enums(text)
    text = remove_attributes(text)
    text = fix_other_cases(text)
    text = remove_inline_stuff(text)
    text = remove_weird_functions(text)
    text = remove_asm_functions(text)
    text = remove_empty_lines(text)
    text = remove_functions(text, ["void SDL_LogMessageV"])
    return text

def main():
    """Entry point"""
    text = run_preprocessor("/usr/local/include/SDL2/SDL.h")
    
    cleaned = clean_header(text)
    with open("fixed_header.h", "w") as f:
        f.write(cleaned)
    
if __name__ == '__main__':
    main()
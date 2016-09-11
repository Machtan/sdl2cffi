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
    return text

def clean_header(text):
    text = remove_non_sdl_parts(text)
    text = remove_enums(text)
    text = remove_empty_lines(text)
    text = remove_attributes(text)
    return text

def main():
    """Entry point"""
    with open("cleaned.h") as f:
        text = f.read()
    
    cleaned = clean_header(text)
    with open("fixed_header.h", "w") as f:
        f.write(cleaned)
    
if __name__ == '__main__':
    main()
import subprocess
import sys
import os
import re
from collections import OrderedDict

RE_TYPEDEF_ENUM = re.compile(r"typedef enum\s+[{]((?:.|\n)+?)\n[}]\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*;")
RE_ENUM = re.compile(r"enum\s+[{]([^}]*?)[}]\s*;")

class Enum:
    def __init__(self, body, typedef=None):
        if typedef:
            pass#print("TYPEDEF ENUM: {}".format(typedef))
        else:
            pass#print("ENUM:")
        self.typedef = typedef
        items = []
        for line in body.split(","):
            if not line.isspace():
                items.append(line.replace("\n", ""))
            #print(line)
        members = OrderedDict()
        for line in items:
            if line == "'": # Handle SDLK_COMMA = ',',
                continue
            if "=" in line:
                #print(line)
                key, value = line.split("=", 1)
                #print("{!r} = {!r}".format(key, value))
                members[key.strip()] = value.strip()
            else:
                members[line.strip()] = None
        self.members = members
    
    def format_c(self):
        lines = []
        if self.typedef:
            lines.append("typedef enum {")
        else:
            lines.append("enum {")
        
        for key, value in self.members.items():
            if value is None:
                lines.append("   {},".format(key))
            else:
                lines.append("   {} = {}, ".format(key, value))
            
        if self.typedef:
            lines.append("}} {};".format(self.typedef))
        else:
            lines.append("};")
        
        return os.linesep.join(lines)
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        if self.typedef:
            return "typedef enum {} {{ ...{} }}".format(self.typedef, len(self.members))
        else:
            key, val = list(self.members.items())[0]
            if val is not None:
                text = "{} = {}".format(key, val)
            else:
                text = key
            return "enum {{ {}, ...{} }}".format(text, len(self.members)-1)

def run_preprocessor(headerfile):
    res = subprocess.run(["cc", "-E", "-P", headerfile], 
        stdout=subprocess.PIPE, universal_newlines=True)
    return res.stdout

def find_enums(text):
    enums = []
    for match in RE_TYPEDEF_ENUM.finditer(text):
        body, typedef = match.groups()
        enum = Enum(body, typedef=typedef)
        enums.append((match.start(), enum))
    
    for match in RE_ENUM.finditer(text):
        body = match.groups()[0]
        enum = Enum(body)
        enums.append((match.start(), enum))
    
    enums.sort()
    return [enum for _, enum in enums]

def generate_c_file(include, enums):
    lines = []
    
    start = """\
#include "{}"

int main(int argc, char** argv) {{\
    """.format(include)
    lines.append(start)
    
    def printf(line, *args):
        if not args:
            argtext = ""
        else:
            argtext = ", " + ", ".join(args)
        lines.append("    printf(\"{}\\n\"{});".format(line, argtext))
    
    printf("{")
    for enum in enums:
        for key in enum.members.keys():
            printf("    \\\"{}\\\": %d,".format(key), key)
    
    printf("}")
    lines.append("}")
    return os.linesep.join(lines)

def save_enums(enums):
    lines = []
    for enum in enums:
        lines.append(enum.format_c())
        lines.append(os.linesep)
    
    return os.linesep.join(lines)

def clean_enums(text, include_path):
    enums = find_enums(text)
    
    ctext = generate_c_file(include_path, enums)
    dirname = os.path.dirname(os.path.abspath(__file__))
    cpath = os.path.join(dirname, "enum_importer.c")
    with open(cpath, "w") as f:
        f.write(ctext)
    
    exepath = os.path.join(dirname, "enum_importer")
    subprocess.run(["cc", "-o", exepath, "-lSDL2", cpath])
    res = subprocess.run([exepath], stdout=subprocess.PIPE, universal_newlines=True)
    values = eval(res.stdout)
    #print(len(values))
    for enum in enums:
        for key in enum.members.keys():
            enum.members[key] = values[key]
    
    enum_text = save_enums(enums)
    return enum_text


def main():
    """Entry point"""
    text = run_preprocessor("/usr/local/include/SDL2/SDL.h")
    enum_text = clean_enums(text, "SDL2/SDL.h")
    with open("fixed_enums.h", "w") as f:
        f.write(enum_text)
    
if __name__ == '__main__':
    main()
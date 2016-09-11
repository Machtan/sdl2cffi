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
            print("TYPEDEF ENUM: {}".format(typedef))
        else:
            print("ENUM:")
        self.typedef = typedef
        items = [part.replace("\n", "") for part in body.split(",\n")]
        members = OrderedDict()
        for line in items:
            if "=" in line:
                print(line)
                key, value = line.split("=", 1)
                members[key.strip()] = value.strip()
            else:
                members[line.strip()] = None
        self.members = members
    
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

def main():
    """Entry point"""
    #text = run_preprocessor("include/SDL.h")
    #print(text)
    with open("cleaned.h") as f:
        text = f.read()
    enums = find_enums(text)
    for enum in enums:
        print(enum)
    
    ctext = generate_c_file("SDL2/SDL.h", enums)
    print(ctext)
    with open("enum_importer.c", "w") as f:
        f.write(ctext)
    
    #if not os.path.exists("enum_importer"):
    subprocess.run(["cc", "-o", "enum_importer", "-lSDL2", "enum_importer.c"])
    res = subprocess.run(["./enum_importer"], stdout=subprocess.PIPE, universal_newlines=True)
    values = eval(res.stdout)
    print(len(values))
    
if __name__ == '__main__':
    main()
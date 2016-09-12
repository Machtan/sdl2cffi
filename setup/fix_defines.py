import os
import sys
import subprocess

def run_preprocessor_with_includes(headerfile):
    res = subprocess.run(["cc", "-E", headerfile], 
        stdout=subprocess.PIPE, universal_newlines=True)
    return res.stdout

IGNORED = set([
    "SDL_FILE",
    "SDL_AUDIOCVT_PACKED",
    "SDL_FORCE_INLINE",
    "SDL_INLINE",
    "SDL_MAIN_AVAILABLE",
    "SDL_MAIN_NEEDED",
    "SDL_PASSED_BEGINTHREAD_ENDTHREAD",
    "SDL_PRINTF_FORMAT_STRING",
    "SDL_SCANF_FORMAT_STRING",
    "SDL_PRIX64",
])
def find_defines(text, defines=None):
    if defines is None:
        defines = set()
    for line in text.splitlines():
        if line.startswith("#define") and not ")" in line:
            parts = line.split(" ")
            if len(parts) < 2:
                continue
            define = line.split(" ")[1].split("\t")[0]
            if not define.startswith("SDL_"):
                continue
            if not define.isupper():
                continue
            if "ANDROID" in define:
                continue
            if define.startswith("SDL_HINT"):
                continue
            if define in IGNORED:
                continue
            #print("Found: {}".format(define))
            #print("  "+line)
            defines.add(define)
            
    return defines

def find_includes(headerfile):
    text = run_preprocessor_with_includes(headerfile)
    includes = set()
    includes.add(headerfile)
    for line in text.splitlines():
        if line.startswith("# "):
            #print(line)
            include = line.split("\"")[1]
            if not include.startswith("<"):
                includes.add(include)
    
    return includes

def generate_c_file(include_path, defines):
    lines = []

    start = """\
#include "{}"

int main(int argc, char** argv) {{\
    """.format(include_path)
    lines.append(start)

    def printf(line, *args):
        if not args:
            argtext = ""
        else:
            argtext = ", " + ", ".join(args)
        lines.append("    printf(\"{}\\n\"{});".format(line, argtext))

    printf("{")
    for define in defines:
        if define.startswith("SDL_HINT"):
            spec = "\\\"%s\\\""
        else:
            spec = "%d"
        printf("    \\\"{}\\\": {},".format(define, spec), define)

    printf("}")
    lines.append("}")
    return os.linesep.join(lines)

def load_values(include_path, defines):
    ctext = generate_c_file(include_path, defines)
    with open("define_importer.c", "w") as f:
        f.write(ctext)
    
    subprocess.run(["cc", "-o", "define_importer", "-lSDL2", "define_importer.c"])
    res = subprocess.run(["./define_importer"], stdout=subprocess.PIPE, universal_newlines=True)
    define_pairs = eval(res.stdout)
    return define_pairs

def clean_defines(headerfile):
    defines = set()
    for path in find_includes(headerfile):
        with open(path) as f:
            text = f.read()
        find_defines(text, defines)
    
    defines = list(sorted(defines))
    return os.linesep.join(["#define {} ...".format(d) for d in defines])

def main():
    """Entry point"""
    text = clean_defines("include/SDL.h")
    with open("fixed_defines.h", "w") as f:
        f.write(text)
        

if __name__ == '__main__':
    main()
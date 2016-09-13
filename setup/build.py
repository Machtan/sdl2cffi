import sys
import os
import subprocess
from cffi import FFI
from fix_header import clean_header
from fix_enums import clean_enums
from fix_defines import clean_defines

LOCAL = os.path.dirname(os.path.abspath(__file__))

def run_preprocessor(headerfile):
    res = subprocess.run(["cc", "-E", "-P", headerfile], 
        stdout=subprocess.PIPE, universal_newlines=True)
    return res.stdout

def main(args=sys.argv[1:]):
    """Entry point"""
    if sys.platform.startswith("win"):
        print("Windows is currently unsupported.")
        print("feel free to add support :)")
        sys.exit(1)
    
    if len(args) < 1:
        print("Usage: python3 build.py <path to SDL.h>")
        sys.exit(1)
    
    header_path = os.path.abspath(args[0])
    if not os.path.exists(header_path):
        print("Header file not found: {!r}".format(args[0]))
        sys.exit(1)
    
    INCLUDE_PATH = "SDL2/SDL.h"
    
    ffibuilder = FFI()
    
    MODULE_NAME = "_sdl2"
    ffibuilder.set_source(MODULE_NAME,
        """
        #include "SDL2/SDL.h"
        #include "SDL2/SDL_image.h"
        """,
        libraries = [
            "SDL2",
            "SDL2_image",
        ]
    )
    
    source_text = run_preprocessor(header_path)
    fixed_defines = clean_defines(header_path)
    fixed_enums = clean_enums(source_text, INCLUDE_PATH)
    fixed_header = clean_header(source_text)
    with open(os.path.join(LOCAL, "manual_image_header.h")) as f:
        image_header = f.read()
        fixed_header = fixed_header + os.linesep + image_header
    
    fixed_source = "{}{}{}{}{}".format(
        fixed_defines,
        os.linesep,
        fixed_enums, 
        os.linesep, 
        fixed_header
    )
    
    ffibuilder.cdef(fixed_source)
    
    libfile = ffibuilder.compile(verbose=True)
    artifacts = [MODULE_NAME + ".c", MODULE_NAME+".o"]
    for artifact in artifacts:
        if os.path.exists(artifact):
            os.remove(artifact)

if __name__ == '__main__':
    main()
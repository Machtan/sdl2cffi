import sys
import os
import subprocess
from cffi import FFI
from fix_header import clean_header
from fix_enums import clean_enums

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
    
    include_path = os.path.relpath(header_path, start="/usr/local/include")
    
    ffibuilder = FFI()

    ffibuilder.set_source("_sdl2",
        """
        #include "SDL2/SDL.h"
        """,
        libraries = [
            "SDL2"
        ]
    )
    
    source_text = run_preprocessor(header_path)
    fixed_enums = clean_enums(source_text, include_path)
    fixed_header = clean_header(source_text)
    fixed_source = "{}{}{}".format(fixed_enums, os.linesep, fixed_header)
    
    ffibuilder.cdef(fixed_source)
    
    ffibuilder.compile(verbose=True)

if __name__ == '__main__':
    main()
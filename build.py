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
    if sys.platform != "darwin":
        print("The program probably only works on OSX!")
        sys.exit(1)
    
    if len(args) < 1:
        print("Usage: python3 build.py <path to SDL.h>")
        sys.exit(1)
    
    header_path = args[0]
    if not os.path.exists(header_path):
        print("Header file not found: {!r}".format(header_path))
        sys.exit(1)
    
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
    fixed_enums = clean_enums(source_text)
    fixed_header = clean_header(source_text)
    fixed_source = "{}{}{}".format(fixed_enums, os.linesep, fixed_header)
    
    ffibuilder.cdef(fixed_source)
    
    ffibuilder.compile(verbose=True)

if __name__ == '__main__':
    main()
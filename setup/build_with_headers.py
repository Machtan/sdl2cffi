from cffi import FFI
import sys
import os

def main():
    """Entry point"""
    if len(sys.argv) < 2:
        return print("Usage: python3 build_with_headers.py <header.h> [<header.h>, ...]")
    
    ffibuilder = FFI()

    ffibuilder.set_source("_sdl2",
        """
        #include "SDL2/SDL.h"
        """,
        libraries = [
            "SDL2"
        ]
    )
    
    cdefs = []
    
    for header in sys.argv[1:]:
        with open(header) as f:
            text = f.read()
            cdefs.append(text)
    
    header_source = os.linesep.join(cdefs)
    
    ffibuilder.cdef(header_source)
    
    ffibuilder.compile(verbose=True)

if __name__ == '__main__':
    main()
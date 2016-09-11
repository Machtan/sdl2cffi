from cffi import FFI
import sys

def main():
    """Entry point"""
    if len(sys.argv) < 2:
        return print("Usage: python3 build_with_header.py <header.h>")
    
    ffibuilder = FFI()

    ffibuilder.set_source("_sdl2",
        """
        #include "SDL2/SDL.h"
        """,
        libraries = [
            "SDL2"
        ]
    )
    
    with open(sys.argv[1]) as f:
        text = f.read()
    
    ffibuilder.cdef(text)
    
    ffibuilder.compile(verbose=True)

if __name__ == '__main__':
    main()
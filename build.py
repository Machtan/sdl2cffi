from cffi import FFI, api

ffibuilder = FFI()

ffibuilder.set_source("_sdl2",
    """
    #include "SDL2/SDL.h"
    """,
    libraries = [
        "SDL2"
    ]
)

simple = """
    typedef uint32_t Uint32;
    
    int SDL_Init(Uint32 flags);
    void SDL_PumpEvents();
    
    typedef struct SDL_Window SDL_Window;
    SDL_Window* SDL_CreateWindow(const char* title,
                                 int         x,
                                 int         y,
                                 int         w,
                                 int         h,
                                 Uint32      flags);
    
    void SDL_Quit();

    #define SDL_INIT_EVERYTHING ...
"""
#ffibuilder.cdef(simple)

import os
from preprocess import process_file
ignore_map = {
    "SDL_stdinc.h": ["function"],
    "SDL_error.h": ["function"],
    "SDL_assert.h": ["function", "typedef", "callback"],
    "SDL_atomic.h": ["function"],
    "SDL_thread.h": ["typedef", "function"],
    "SDL_rwops.h": [],
}

header = "include/SDL_video.h"
header = "include/SDL.h"
excluded = set([])
output = process_file(header, excluded=excluded, ignore_map=ignore_map, recursive=True)
try:
    ffibuilder.cdef(output)

except api.CDefError as e:
    import sys
    print(e.args)
    text, desc = e.args[0].split("\n")
    search = text.split("\"")[1]
    line = desc.split(":")[1]
    print(e.args[0])
    context = "unknown"
    for i, line in enumerate(output.splitlines()):
        if line.startswith("// =="):
            context = line
        if search in line:
            print(context)
            #print("LINE INDEX: {}".format(i))
            print(line)
            print("^" + "~" * (len(line)-1))
    
    sys.exit()

except Exception as e:
    import sys
    print(e.args)
    text, desc = e.args[0].split("\n")
    search = text.split("\"")[1]
    line, col = desc.split(":")[1:3]
    print(e.args[0])
    context = "unknown"
    for i, line in enumerate(output.splitlines()):
        if line.startswith("// =="):
            context = line
        if search in line:
            print(context)
            #print("LINE INDEX: {}".format(i))
            print(line)
            print((int(col)-1)*"~" + "^")
    sys.exit()




if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
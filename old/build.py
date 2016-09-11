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

rwops = """
// ========== stdinch.h for RWOPS =============
typedef int8_t  Sint8;
typedef uint8_t  Uint8;
typedef int16_t  Sint16;
typedef uint16_t  Uint16;
typedef int32_t  Sint32;
typedef uint32_t  Uint32;
typedef int64_t  Sint64;
typedef uint64_t  Uint64;
typedef int  SDL_dummy_;
typedef enum
{
    SDL_FALSE = 0,
    SDL_TRUE = 1
} SDL_bool;

// ========== HANDWRITTEN RWOPS ===============
typedef struct SDL_RWops
{
    /**
     *  Return the size of the file in this rwops, or -1 if unknown
     */
    Sint64 ( * size) (struct SDL_RWops * context);

    /**
     *  Seek to \c offset relative to \c whence, one of stdio's whence values:
     *  RW_SEEK_SET, RW_SEEK_CUR, RW_SEEK_END
     *
     *  \return the final offset in the data stream, or -1 on error.
     */
    Sint64 ( * seek) (struct SDL_RWops * context, Sint64 offset,
                             int whence);

    /**
     *  Read up to \c maxnum objects each of size \c size from the data
     *  stream to the area pointed at by \c ptr.
     *
     *  \return the number of objects read, or 0 at error or end of file.
     */
    size_t ( * read) (struct SDL_RWops * context, void *ptr,
                             size_t size, size_t maxnum);

    /**
     *  Write exactly \c num objects each of size \c size from the area
     *  pointed at by \c ptr to data stream.
     *
     *  \return the number of objects written, or 0 at error or end of file.
     */
    size_t ( * write) (struct SDL_RWops * context, const void *ptr,
                              size_t size, size_t num);

    /**
     *  Close and free an allocated SDL_RWops structure.
     *
     *  \return 0 if successful or -1 on write error when flushing data.
     */
    int ( * close) (struct SDL_RWops * context);

    Uint32 type;
    union
    {
        struct
        {
            SDL_bool autoclose;
            FILE *fp;
        } stdio;

        struct
        {
            Uint8 *base;
            Uint8 *here;
            Uint8 *stop;
        } mem;
        struct
        {
            void *data1;
            void *data2;
        } unknown;
    } hidden;

} SDL_RWops;
"""

import os
from preprocess import process_file
ignore_map = {
    "SDL_stdinc.h": ["function"],
    "SDL_error.h": [],
    "SDL_assert.h": ["function", "typedef", "callback"],
    "SDL_atomic.h": ["function"],
    "SDL_thread.h": ["typedef", "function"],
    "SDL_rwops.h": ["typedef", "struct", "callback"],
}

header = "include/SDL_video.h"
header = "include/SDL.h"
exclude_files = [
    "mutex",
    "endian",
]
excluded = set()
for f in exclude_files:
    path = os.path.abspath(os.path.join("include", "SDL_{}.h".format(f)))
    excluded.add(path)

output = process_file(header, excluded=excluded, ignore_map=ignore_map, recursive=True)
output = rwops + "\n" + output

output_file = "generated.h"
try:
    ffibuilder.cdef(output)

except api.CDefError as e:
    with open(output_file, "w") as f:
        f.write(output)
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
    with open(output_file, "w") as f:
        f.write(output)
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
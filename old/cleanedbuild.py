from cffi import FFI, api
import os

ffibuilder = FFI()

ffibuilder.set_source("_sdl2",
    """
    #include "SDL2/SDL.h"
    """,
    libraries = [
        "SDL2"
    ]
)

with open("cleaned.h") as f:
    text = f.read()

# Remove things before SDL types (SDL_Bool) (add SDL_GetPlatform manually)
# Remove nonextern inline stuff
# Remove SDL_Log*

text = text.replace("extern __attribute__ ((visibility(\"default\"))) ", "")
text = text.replace("__attribute__((always_inline)) ", "")
text = text.replace("__attribute__((packed)) ", "")
text = text.replace("__attribute__", "//")
lines = []
was_empty = False
for line in text.splitlines():
    if line == "" or line.isspace():
        if not was_empty:
            was_empty = True
            lines.append(line)
        else:
            continue
    else:
        was_empty = False
        lines.append(line)

text = os.linesep.join(lines)

with open("cleaned_gen.h", "w") as f:
    f.write(text)

ffibuilder.cdef(text)

if __name__ == '__main__':
    ffibuilder.compile(verbose=True)
import time

import sdl2
from events import get_events, Quit
from window import WindowBuilder

def test():
    from _sdl2 import ffi, lib
    
    print("Init everything: {}".format(lib.SDL_INIT_EVERYTHING))

    lib.SDL_Init(lib.SDL_INIT_EVERYTHING)
    title = b"cffi test!"
    window = lib.SDL_CreateWindow(title, 100, 100, 500, 500, 0)

    while True:
        lib.SDL_PumpEvents()
        time.sleep(0.1)

    lib.SDL_Quit()

def main():
    """Entry point"""
    with sdl2.init_everything():
        print("RUN GAME!")
        window = WindowBuilder().title("Test Game").build()
        loop = True
        while loop:
            for event in get_events():
                if type(event) == Quit:
                    loop = False
                else:
                    print(event)
            
            time.sleep(0.1)
        

if __name__ == '__main__':
    main()


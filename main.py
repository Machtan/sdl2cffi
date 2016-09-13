import time

import sdl2
from events import get_events, Quit
from window import WindowBuilder
from rect import Rect

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
        renderer = window.build_renderer().build()
        renderer.set_clear_color(255, 255, 255)
        loop = True
        rect = Rect(100, 100, 300, 300)
        while loop:
            for event in get_events():
                if type(event) == Quit:
                    loop = False
                else:
                    pass
                    #print(event)
            
            renderer.clear()
            renderer.c_fill_rect((255, 0, 0), rect)
            renderer.present()
            time.sleep(0.1)
        

if __name__ == '__main__':
    main()


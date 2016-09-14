import time

from sdl2cffi import init_everything, get_events, WindowBuilder, Rect, Font
from sdl2cffi.events import Quit

def test():
    from ._sdl2 import ffi, lib
    
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
    with init_everything():
        print("RUN GAME!")
        window = WindowBuilder().title("Test Game").build()
        renderer = window.build_renderer().build()
        sloth = renderer.load_texture("Sloth.png")
        sloth_rect = Rect(300, 100, 128, 128)
        renderer.set_clear_color(255, 255, 255)
        rect = Rect(100, 100, 100, 100)
        
        font = Font.load("/Library/Fonts/Copperplate.ttc", 32)
        surf = font.render_blended("Hello, world!", (0, 255, 0))
        tex = renderer.create_texture_from_surface(surf)
        tex_rect = Rect(100, 300, tex.width, tex.height)
        
        loop = True
        while loop:
            for event in get_events():
                if type(event) == Quit:
                    loop = False
                else:
                    pass
                    #print(event)
            
            renderer.clear()
            renderer.c_fill_rect((255, 0, 0), rect)
            renderer.copy(sloth, dst_rect=sloth_rect)
            renderer.copy(tex, dst_rect=tex_rect)
            renderer.present()
            time.sleep(0.1)        

if __name__ == '__main__':
    main()


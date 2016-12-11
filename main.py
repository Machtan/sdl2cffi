import time

from sdl2 import init_everything, WindowBuilder, Rect, Font, Keycode, Scancode
from sdl2.events import Quit, KeyDown

ITERATIONS = 1000000
def test_rects():
    """
    ITERATIONS = 10000000
    CFFI rect updated every time: 3.3966338299978815
    CFFI rect updated on read: 2.492750878998777
    """
    from _sdl2 import ffi, lib
    class Raw:
        def __init__(self, ptr):
            self.ptr = ptr
    
    class Rect:
        
        @property
        def right(self):
            return self.x + self.w
        
        def __init__(self):
            self.x = 0
            self.y = 0
            self.w = 0
            self.h = 0
    
    class Test:
        def __init__(self, ptr):
            self = ptr
        
        def method(self):
            print("It works! (x: {})".format(self.x))
    
    start = time.perf_counter()
    raw = Raw(ffi.new("SDL_Rect *"))
    for i in range(ITERATIONS):
        raw.ptr.x += 1
    
    elapsed = time.perf_counter() - start
    print("CFFI rect updated every time: {}".format(elapsed))
    
    
    start = time.perf_counter()
    raw = Raw(ffi.new("SDL_Rect *"))
    r = raw.ptr
    for i in range(ITERATIONS):
        r.x += 1
    
    elapsed = time.perf_counter() - start
    print("CFFI rect updated with alias: {}".format(elapsed))
    
    start = time.perf_counter()
    raw = ffi.new("SDL_Rect *")
    rect = Rect()
    for i in range(ITERATIONS):
        rect.x += 1
    raw.x = rect.x
    raw.y = rect.y
    raw.w = rect.w
    raw.h = rect.h
    elapsed = time.perf_counter() - start
    print("CFFI rect updated on read: {}".format(elapsed))
    
    start = time.perf_counter()
    raw = ffi.new("SDL_Rect *")
    rect = Test(raw)
    rect.method()
    for i in range(ITERATIONS):
        rect.x += 1
    
    elapsed = time.perf_counter() - start
    print("Test: {}".format(elapsed))

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
    with init_everything() as context:
        print("RUN GAME!")
        window = context.build_window().title("Test Game").finish()
        renderer = window.build_renderer().finish()
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
            for event in context.get_events():
                if type(event) == KeyDown:
                    print("Keydown: key:  {}".format(Keycode.name(event.keycode)))
                    print("         scan: {}".format(Scancode.name(event.scancode)))
                    scan = Keycode.to_scancode(event.keycode)
                    name = Scancode.name(scan)
                    print("Mapped scan name: {}".format(name))
            
            renderer.clear()
            renderer.color((255, 0, 0)).fill_rect(rect)
            renderer.copy(sloth, dst_rect=sloth_rect)
            renderer.copy(tex, dst_rect=tex_rect)
            renderer.present()
            time.sleep(0.1)
    
    print("After Context is finished")     

if __name__ == '__main__':
    main()


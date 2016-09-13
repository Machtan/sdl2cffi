from _sdl2 import lib, ffi
from common import SDLAllocated, assert_non_null, assert_zero

class Renderer(SDLAllocated(lib.SDL_DestroyRenderer)):
    def __init__(self, raw):
        self._raw = raw
        self.clear_color = (0, 0, 0, 255)
    
    def set_clear_color(self, r, g, b, a=255):
        self.clear_color = (r, g, b, a)
    
    def set_draw_color(self, r, g, b, a=255):
        assert_zero(lib.SDL_SetRenderDrawColor(self._raw, r, g, b, a))
    
    def clear(self, color=None):
        if color is not None:
            self.set_draw_color(*color)
        else:
            self.set_draw_color(*self.clear_color)
        assert_zero(lib.SDL_RenderClear(self._raw))
    
    def c_fill_rect(self, color, rect):
        self.set_draw_color(*color)
        self.fill_rect(rect)
    
    def fill_rect(self, rect):
        assert_zero(lib.SDL_RenderFillRect(self._raw, rect._raw))      
    
    def present(self):
        lib.SDL_RenderPresent(self._raw)

class RendererBuilder:
    def __init__(self, window):
        self._window = window
        self._index = -1
        self._flags = 0
    
    def build(self):
        raw = assert_non_null(lib.SDL_CreateRenderer(self._window._raw, self._index, self._flags))
        return Renderer(raw)
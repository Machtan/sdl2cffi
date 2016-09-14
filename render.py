from ._sdl2 import lib, ffi
from .common import Allocated, assert_non_null, assert_zero

class Texture(Allocated(lib.SDL_DestroyTexture)):
    def __init__(self, raw):
        super().__init__()
        self._raw = raw
        wptr = ffi.new("int *")
        hptr = ffi.new("int *")
        assert_zero(lib.SDL_QueryTexture(raw, ffi.NULL, ffi.NULL, wptr, hptr))
        self.width = wptr[0]
        self.height = hptr[0]

class Renderer(Allocated(lib.SDL_DestroyRenderer)):
    def __init__(self, raw):
        super().__init__()
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
    
    def load_texture(self, filepath):
        """Loads the image in the given file as a texture"""
        rawpath = bytes(filepath, encoding="utf8")
        raw = assert_non_null(lib.IMG_LoadTexture(self._raw, rawpath))
        return Texture(raw)
    
    def create_texture_from_surface(self, surface):
        raw = assert_non_null(lib.SDL_CreateTextureFromSurface(self._raw, surface._raw))
        return Texture(raw)
    
    def copy(self, texture, src_rect=None, dst_rect=None):
        """Renders the source part of the texture at destination.
        If no source area is given, the whole texture is used.
        If no destination is given, the texture is stretched and the whole area
        is filled"""
        src = src_rect._raw if src_rect is not None else ffi.NULL
        dst = dst_rect._raw if dst_rect is not None else ffi.NULL
        assert_zero(lib.SDL_RenderCopy(self._raw, texture._raw, src, dst))
    
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
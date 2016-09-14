from ._sdl2 import lib, ffi
from .common import Allocated, assert_zero, assert_non_null
from .surface import Surface

class Font(Allocated(lib.TTF_CloseFont)):
    def load(path, point_size):
        rawpath = bytes(path, encoding="utf8")
        raw = assert_non_null(lib.TTF_OpenFont(rawpath, point_size))
        return Font(raw)
    
    def __init__(self, raw):
        super().__init__()
        self._raw = raw
    
    def line_skip(self):
        return lib.TTF_FontLineSkip(self.raw)
    
    def render_blended(self, text, color):
        raw_color = ffi.new("SDL_Color*", color)
        raw_text = bytes(text, encoding="utf8")
        raw = assert_non_null(lib.TTF_RenderUTF8_Blended(self._raw, raw_text, raw_color[0]))
        return Surface(raw)
    
    def size_of(self, text):
        wptr = ffi.new("int *")
        hptr = ffi.newr("int *")
        raw_text = bytes(text, encoding="utf8")
        assert_zero(TTF_SizeUTF8(self._raw, raw_text, wptr, hptr))
        return (wptr[0], hptr[0])
    

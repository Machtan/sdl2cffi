from ._sdl2 import lib, ffi
from .common import Allocated, assert_zero, assert_nonnull
from .surface import Surface

class Font(Allocated):
    def load(path, point_size):
        rawpath = bytes(path, encoding="utf8")
        raw = assert_nonnull(lib.TTF_OpenFont(rawpath, point_size))
        return Font(raw)
    
    def __init__(self, raw, *args):
        if len(args) > 0:
            raise ValueError("Font.__init__ should not be called: Use Font.load!")
        super().__init__(lib.TTF_CloseFont)
        self._raw = raw
    
    def line_skip(self):
        return lib.TTF_FontLineSkip(self._raw)
    
    def render_blended(self, text, color):
        raw_color = ffi.new("SDL_Color*", color)
        raw_text = bytes(text, encoding="utf8")
        raw = assert_nonnull(lib.TTF_RenderUTF8_Blended(self._raw, raw_text, raw_color[0]))
        return Surface(raw)
    
    def render_shaded(self, text, fgcolor, bgcolor):
        raw_fg = ffi.new("SDL_Color*", fgcolor)
        raw_bg = ffi.new("SDL_Color*", bgcolor)
        raw_text = bytes(text, encoding="utf8")
        raw = assert_nonnull(lib.TTF_RenderUTF8_Shaded(self._raw, raw_text, raw_fg[0], raw_bg[0]))
        return Surface(raw)
    
    def size_of(self, text):
        wptr = ffi.new("int *")
        hptr = ffi.newr("int *")
        raw_text = bytes(text, encoding="utf8")
        assert_zero(TTF_SizeUTF8(self._raw, raw_text, wptr, hptr))
        return (wptr[0], hptr[0])
    

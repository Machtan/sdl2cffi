from ._sdl2 import lib, ffi
from .common import Allocated, assert_zero, assert_nonnull
from .surface import Surface
from .types import Color, Size

class Font(Allocated):
    """A TrueType font"""
    # TODO: find out how to tell mypy that this is static
    def load(path: str, point_size: int): # TODO forward return
        """Loads the font at the given path in the given point size in pixels.
        Only TrueType fonts are supported."""
        rawpath = bytes(path, encoding="utf8")
        raw = assert_nonnull(lib.TTF_OpenFont(rawpath, point_size))
        return Font(raw)
    
    def __init__(self, raw, *args):
        if len(args) > 0:
            raise ValueError("Font.__init__ should not be called: Use Font.load!")
        super().__init__(lib.TTF_CloseFont)
        self._raw = raw
    
    def line_skip(self) -> int:
        """Returns the recommended line height for lines of text in this font.
        Use this to space rendered lines nicely"""
        return lib.TTF_FontLineSkip(self._raw)
    
    def render_blended(self, text: str, color: Color) -> Surface:
        """Renders the given text aliased in a way that looks good on all
        backgrounds. This is a little slower than 'Font.render_shaded'"""
        raw_color = ffi.new("SDL_Color*", color)
        raw_text = bytes(text, encoding="utf8")
        raw = assert_nonnull(lib.TTF_RenderUTF8_Blended(self._raw, raw_text, raw_color[0]))
        return Surface(raw)
    
    def render_shaded(self, text: str, fgcolor: Color, bgcolor: Color) -> Surface:
        """Renders the given text aliased in a way that looks good on top of
        backgrounds in the given background color"""
        raw_fg = ffi.new("SDL_Color*", fgcolor)
        raw_bg = ffi.new("SDL_Color*", bgcolor)
        raw_text = bytes(text, encoding="utf8")
        raw = assert_nonnull(lib.TTF_RenderUTF8_Shaded(self._raw, raw_text, raw_fg[0], raw_bg[0]))
        return Surface(raw)
    
    def size_of(self, text: str) -> Size:
        """Returns the width and height of the given text rendered using this
        font"""
        wptr = ffi.new("int *")
        hptr = ffi.newr("int *")
        raw_text = bytes(text, encoding="utf8")
        assert_zero(lib.TTF_SizeUTF8(self._raw, raw_text, wptr, hptr))
        return (wptr[0], hptr[0])
    

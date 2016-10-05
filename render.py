from ._sdl2 import lib, ffi
from .common import Allocated, assert_nonnull, assert_zero

class Texture(Allocated(lib.SDL_DestroyTexture)):
    def __init__(self, raw):
        super().__init__()
        self._raw = raw
        wptr = ffi.new("int *")
        hptr = ffi.new("int *")
        assert_zero(lib.SDL_QueryTexture(raw, ffi.NULL, ffi.NULL, wptr, hptr))
        self.width = wptr[0]
        self.height = hptr[0]


class BlendMode:
    None_ = lib.SDL_BLENDMODE_NONE
    Blend = lib.SDL_BLENDMODE_BLEND
    Add = lib.SDL_BLENDMODE_ADD
    Mod = lib.SDL_BLENDMODE_MOD


class Renderer(Allocated(lib.SDL_DestroyRenderer)):
    def __init__(self, raw, *args):
        if len(args) > 0:
            raise ValueError("Renderer.__init__ should not be called: Use Window.build_renderer(self)!")
        super().__init__()
        self._raw = raw
        self.clear_color = (0, 0, 0, 255)
    
    def set_clear_color(self, r, g, b, a=255):
        self.clear_color = (r, g, b, a)
    
    def set_draw_color(self, r, g, b, a=255):
        assert_zero(lib.SDL_SetRenderDrawColor(self._raw, r, g, b, a))
    
    def set_blend_mode(self, mode):
        assert_zero(lib.SDL_SetRenderDrawEBlendMode(mode))
    
    def clear(self, color=None):
        if color is not None:
            self.set_draw_color(*color)
        else:
            self.set_draw_color(*self.clear_color)
        assert_zero(lib.SDL_RenderClear(self._raw))
    
    def load_texture(self, filepath):
        """Loads the image in the given file as a texture"""
        rawpath = bytes(filepath, encoding="utf8")
        raw = assert_nonnull(lib.IMG_LoadTexture(self._raw, rawpath))
        return Texture(raw)
    
    def create_texture_from_surface(self, surface):
        raw = assert_nonnull(lib.SDL_CreateTextureFromSurface(self._raw, surface._raw))
        return Texture(raw)
    
    def copy(self, texture, src_rect=None, dst_rect=None):
        """Renders the source part of the texture at destination.
        If no source area is given, the whole texture is used.
        If no destination is given, the texture is stretched and the whole area
        is filled"""
        src = src_rect._raw if src_rect is not None else ffi.NULL
        dst = dst_rect._raw if dst_rect is not None else ffi.NULL
        assert_zero(lib.SDL_RenderCopy(self._raw, texture._raw, src, dst))
    
    def copy_ex(self, texture, src_rect=None, dst_rect=None, angle=0,
            center=None, flip_hor=False, flip_ver=False):
        """Renders the source part of the texture at destination, optionally 
        rotating and/or flipping it.
        The 'flip' argument should be a 'EFlip' enum value.
        If no source area is given, the whole texture is used.
        If no destination is given, the texture is stretched and the whole area
        is filled.
        If no rotation center is given, the center of the dst_rect is used."""
        src = src_rect._raw if src_rect is not None else ffi.NULL
        dst = dst_rect._raw if dst_rect is not None else ffi.NULL
        center = ffi.new("SDL_Point *", center) if center is not None else ffi.NULL
        hflip = lib.SDL_FLIP_HORIZONTAL if flip_hor else 0
        vflip = lib.SDL_FLIP_VERTICAL if flip_ver else 0
        assert_zero(lib.SDL_RenderCopyEx(
            self._raw, texture._raw, src, dst, angle, center, 
            hflip | vflip
        ))
    
    def set_clip_rect(self, rect):
        """Sets the clip rect of the renderer to the given rect.
        To disable the clip_rect, use Rect.disable_clip_rect"""
        assert_zero(lib.SDL_RenderSetClipRect(self._raw, rect._raw))
    
    def disable_clip_rect(self):
        """Disables the clip rect for this renderer"""
        assert_zero(lib.SDL_RenderSetClipRect(self._raw, ffi.NULL))
    
    def fill_rect(self, rect):
        """Fills a rectangular area with the current drawing color"""
        assert_zero(lib.SDL_RenderFillRect(self._raw, rect._raw))
    
    def draw_rect(self, rect):
        """Draws the outline of a rectangular area with the current drawing color"""
        assert_zero(lib.SDL_RenderDrawRect(self._raw, rect._raw))
    
    def draw_line(self, x1, y1, x2, y2):
        assert_zero(lib.SDL_RenderDrawLine(self._raw, x1, y1, x2, y2))
    
    def draw_point(self, x, y):
        assert_zero(lib.SDL_RenderDrawPoint(self._raw, x, y))
    
    def c_fill_rect(self, color, rect):
        self.set_draw_color(*color)
        self.fill_rect(rect)
    
    def c_draw_rect(self, color, rect):
        self.set_draw_color(*color)
        self.draw_rect(rect)
    
    def c_draw_line(self, color, x1, y1, x2, y2):
        self.set_draw_color(*color)
        self.draw_line(x1, y1, x2, y2)
    
    def c_draw_point(self, color, x, y):
        self.set_draw_color(*color)
        self.draw_point(x, y)
    
         
    
    def present(self):
        lib.SDL_RenderPresent(self._raw)

class RendererBuilder:
    """A builder for renderers."""
    def __init__(self, window):
        self._window = window
        self._index = -1
        self._flags = 0
    
    def finish(self):
        """Builds the renderer and returns it"""
        raw = assert_nonnull(lib.SDL_CreateRenderer(self._window._raw, self._index, self._flags))
        return Renderer(raw)
    
    def build(self):
        print("Warning: RendererBuilder.build is deprecated, use .finish!")
        return self.finish()
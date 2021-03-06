from ._sdl2 import lib, ffi
from .common import SdlRef, assert_nonnull, assert_zero
from .rect import Rect
from .surface import Surface
from .types import Color, Point
from typing import Optional, Union, Tuple, Any

class Texture:
    """A GPU-uploaded 'image' (buffer of pixel data)"""
    def __init__(self, ref: SdlRef):
        self._ref = ref
        self._raw = ref._raw
        wptr = ffi.new("int *")
        hptr = ffi.new("int *")
        assert_zero(lib.SDL_QueryTexture(ref._raw, ffi.NULL, ffi.NULL, wptr, hptr))
        self.width = wptr[0]
        self.height = hptr[0]
    
    def rect(self):
        """Returns a rectangle with the size of this texture"""
        return Rect(0, 0, self.width, self.height)
    
    def rect_at(self, x: int, y: int):
        """Returns a rectangle with the size of this texture at the given position"""
        return Rect(x, y, self.width, self.height)


class BlendMode(int):
    """Blend mode enumeration."""
    None_ = lib.SDL_BLENDMODE_NONE
    Blend = lib.SDL_BLENDMODE_BLEND
    Add = lib.SDL_BLENDMODE_ADD
    Mod = lib.SDL_BLENDMODE_MOD

class ClipContext:
    """A context in which the renderer has the given clip rect"""
    def __init__(self, renderer, rect):
        self._renderer = renderer
        self._rect = rect
    
    def __enter__(self):
        self._renderer.push_clip_rect(self._rect)
        return self._renderer
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._renderer.pop_clip_rect()

class Renderer:
    def __init__(self, ref: SdlRef, *args):
        if len(args) > 0:
            raise ValueError("Renderer.__init__ should not be called: Use Window.build_renderer(self)!")
        self._ref = ref
        self._raw = ref._raw
        self._clear_color = (0, 0, 0, 255)
        self._clip_rects = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def set_clear_color(self, r: int, g: int, b: int, a: int=255):
        """Sets the color that the renderer fills the screen with after calls
        to Renderer.clear. (The background color of each frame)."""
        self._clear_color = (r, g, b, a)
    
    def set_draw_color(self, r: int, g: int, b: int, a: int=255):
        """Sets the draw color for the renderer, that primitives will be
        drawn with afterwards."""
        assert_zero(lib.SDL_SetRenderDrawColor(self._raw, r, g, b, a))
    
    def offset_context(self, dx: int, dy: int, force=False) -> Any:
        """Returns a context in which the renderer is offset by the given amount.
        Use 'force' to always create an offset renderer (cheaper for scene graphs)"""
        if dx == 0 and dy == 0 and not force:
            return self
        else:
            return OffsetRenderer(self, dx, dy)
    
    # TODO: Is this typing correct?
    def set_blend_mode(self, mode: BlendMode):
        """Sets the blend mode of the renderer.
        I'm not really sure what it does. (probably something about transparency
        and how to combine transparent colors.)"""
        assert_zero(lib.SDL_SetRenderDrawEBlendMode(mode))
    
    def clear(self, color: Optional[Color]=None):
        """Clears the screen with the given color, or the current clear color
        if nothing is given."""
        if color is not None:
            self.set_draw_color(*color)
        else:
            self.set_draw_color(*self._clear_color)
        assert_zero(lib.SDL_RenderClear(self._raw))
    
    def load_texture(self, filepath: str) -> Texture:
        """Loads the image in the given file as a texture"""
        rawpath = bytes(filepath, encoding="utf8")
        raw = assert_nonnull(lib.IMG_LoadTexture(self._raw, rawpath))
        ref = SdlRef(raw, lib.SDL_DestroyTexture)
        return Texture(ref)
    
    def create_texture_from_surface(self, surface: Surface) -> Texture:
        """Creates a Texture from a given Surface."""
        raw = assert_nonnull(lib.SDL_CreateTextureFromSurface(self._raw, surface._raw))
        ref = SdlRef(raw, lib.SDL_DestroyTexture)
        return Texture(ref)
    
    def copy(self, texture: Texture, src_rect: Optional[Rect]=None, 
            dst_rect: Optional[Rect]=None):
        """Renders the source part of the texture at destination.
        If no source area is given, the whole texture is used.
        If no destination is given, the texture is stretched and the whole area
        is filled"""
        src = src_rect._raw if src_rect is not None else ffi.NULL
        dst = dst_rect._raw if dst_rect is not None else ffi.NULL
        assert_zero(lib.SDL_RenderCopy(self._raw, texture._raw, src, dst))
    
    def copy_ex(self, texture: Texture, src_rect: Optional[Rect]=None,
            dst_rect: Optional[Rect]=None, angle:int=0,
            center: Optional[Point]=None, flip_hor: bool=False, 
            flip_ver: bool=False):
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
    
    def set_clip_rect(self, rect: Rect):
        """Sets the clip rect of the renderer to the given rect.
        To disable the clip_rect, use Rect.disable_clip_rect"""
        assert_zero(lib.SDL_RenderSetClipRect(self._raw, rect._raw))
    
    def disable_clip_rect(self):
        """Disables the clip rect for this renderer"""
        assert_zero(lib.SDL_RenderSetClipRect(self._raw, ffi.NULL))
    
    def clipped(self, rect: Rect) -> ClipContext:
        """Returns a context in which the rendering is clipped to the given rect"""
        return ClipContext(self, rect)
    
    def push_clip_rect(self, rect: Rect):
        """Pushes the given rect as a clip rect for the renderer"""
        self._clip_rects.append(rect)
        self.set_clip_rect(rect)
    
    def pop_clip_rect(self) -> Rect:
        """Pops the current clip rect of the renderer and returns it,
        setting the clip rect to the next one, or disabling it"""
        if not self._clip_rects:
            raise ValueError("Attempted to pop clip rect with none active!")
        popped = self._clip_rects.pop()
        if not self._clip_rects:
            self.disable_clip_rect()
        else:
            self.set_clip_rect(self._clip_rects[-1])
        return popped
    
    def color(self, color: Color) -> Any:
        """Sets the draw color of the renderer and returns it."""
        self.set_draw_color(*color)
        return self
    
    def fill_rect(self, rect: Rect):
        """Fills a rectangular area with the current draw color"""
        assert_zero(lib.SDL_RenderFillRect(self._raw, rect._raw))
    
    def draw_rect(self, rect: Rect):
        """Draws the outline of a rectangular area with the current draw color"""
        assert_zero(lib.SDL_RenderDrawRect(self._raw, rect._raw))
    
    def draw_line(self, x1: int, y1: int, x2: int, y2: int):
        """Draws a line from (x1, y1) to (x2, y2) using the current draw color"""
        assert_zero(lib.SDL_RenderDrawLine(self._raw, x1, y1, x2, y2))
    
    def draw_point(self, x: int, y: int):
        """Fills the pixel at (x, y) with the current draw color"""
        assert_zero(lib.SDL_RenderDrawPoint(self._raw, x, y))
    
    def present(self):
        """Sends the current frame to the GPU for drawing"""
        lib.SDL_RenderPresent(self._raw)

class OffsetContext:
    def __init__(self, offset_renderer, x_offset: int, y_offset: int):
        self.offset_renderer = offset_renderer
        self._x_offset = x_offset
        self._y_offset = y_offset
    
    def __enter__(self):
        self.offset_renderer.x_offset += self._x_offset
        self.offset_renderer.y_offset += self._y_offset
        return self.offset_renderer
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.offset_renderer.x_offset -= self._x_offset
        self.offset_renderer.y_offset -= self._y_offset

# TODO: Finish implementing
class OffsetRenderer(Renderer):
    """A renderer that has been offset by a small amount"""
    def __init__(self, original, x_offset, y_offset, *args):
        super().__init__(original._ref, *args)
        self._original = original
        self._clip_rects = original._clip_rects
        self._x_offset = x_offset
        self._y_offset = y_offset
    
    def set_clear_color(self, r: int, g: int, b: int, a: int=255):
        super().set_clear_color(r, g, b, a=a)
        original.set_clear_color(r, g, b, a=a)
    
    def offset_context(self, dx: int, dy: int, force=False) -> OffsetContext:
        """Force is ignored."""
        if dx == 0 or dy == 0:
            return self
        else:
            return OffsetContext(self, dx, dy)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class RendererBuilder:
    """A builder of renderers."""
    def __init__(self, window):
        self._window = window
        self._index = -1
        self._flags = 0
    
    def finish(self) -> Renderer:
        """Builds the renderer and returns it"""
        raw = assert_nonnull(lib.SDL_CreateRenderer(self._window._raw, self._index, self._flags))
        ref = SdlRef(raw, lib.SDL_DestroyRenderer)
        return Renderer(ref)
    
    def build(self) -> Renderer:
        print("Warning: RendererBuilder.build is deprecated, use .finish!")
        return self.finish()

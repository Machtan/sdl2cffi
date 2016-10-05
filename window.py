from ._sdl2 import ffi, lib
from .render import RendererBuilder
from .common import Allocated, assert_nonnull

class Window(Allocated(lib.SDL_DestroyWindow)):
    def __init__(self, raw, *args):
        if len(args) > 0:
            raise ValueError("Window.__init__ should not be called: Use Window.build()!")
        super().__init__()
        self._raw = raw
    
    def build():
        """Starts building a new window""" 
        return WindowBuilder()
    
    def build_renderer(self):
        """Starts building a renderer, rendering to this window."""
        return RendererBuilder(self)

class WindowBuilder():
    def __init__(self):
        self._x = lib.SDL_WINDOWPOS_CENTERED
        self._y = lib.SDL_WINDOWPOS_CENTERED
        self._title = "My SDL2 Game"
        self._width = 500
        self._height = 500
        self._flags = 0
    
    def title(self, title):
        """Sets the title of the window"""
        self._title = title
        return self
    
    def x(self, x):
        """Sets the x position of the window (in pixels)"""
        self._x = x
        return self
    
    def y(self, y):
        """Sets the y position of the window (in pixels)"""
        self._y = y
        return self
    
    def center(self, x=True, y=True):
        """Centers the window on both or one axis"""
        if x:
            self._x = lib.SDL_WINDOWPOS_CENTERED
        if y:
            self._y = lib.SDL_WINDOWPOS_CENTERED
        return self
    
    def w(self, w):
        """Sets the width of the window (in pixels)"""
        self._width = w
        return self
    
    def h(self, h):
        """Sets the height of the window (in pixels)"""
        self._height = h
        return self
    
    def finish(self):
        """Finishes building the window"""
        raw = assert_nonnull(lib.SDL_CreateWindow(
            bytes(self._title, encoding="utf8"), self._x, 
            self._y, self._width, self._height, self._flags
        ))
        return Window(raw)
    
    def build(self):
        print("Warning: WindowBuilder.build is deprecated, use .finish!")
        return self.finish()

from _sdl2 import ffi, lib
from render import RendererBuilder
from common import SDLAllocated, assert_non_null

class Window(SDLAllocated(lib.SDL_DestroyWindow)):
    def __init__(self, raw):
        self._raw = raw    
    
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
        self._title = title
        return self
    
    def x(self, x):
        self._x = x
        return self
    
    def y(self, y):
        self._y = y
        return self
    
    def center(self, x=True, y=True):
        if x:
            self._x = lib.SDL_WINDOWPOS_CENTERED
        if y:
            self._y = lib.SDL_WINDOWPOS_CENTERED
        return self
    
    def w(self, w):
        self._width = w
        return self
    
    def h(self, h):
        self._height = h
        return self
    
    def build(self):
        """Finishes building the window"""
        raw = assert_non_null(lib.SDL_CreateWindow(
            bytes(self._title, encoding="utf8"), self._x, 
            self._y, self._width, self._height, self._flags
        ))
        return Window(raw)

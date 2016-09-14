from ._sdl2 import lib, ffi

class Rect:
    def __init__(self, x, y, w, h):
        self._raw = ffi.new("SDL_Rect *", [x, y, w, h])
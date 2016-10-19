from ._sdl2 import lib, ffi
from .common import Allocated, assert_zero, assert_nonnull

class Surface(Allocated):
    def __init__(self, raw):
        super().__init__(lib.SDL_FreeSurface)
        self._raw = raw
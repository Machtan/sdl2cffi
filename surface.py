from ._sdl2 import lib, ffi
from .common import Allocated, assert_zero, assert_non_null

class Surface(Allocated(lib.SDL_FreeSurface)):
    def __init__(self, raw):
        super().__init__()
        self._raw = raw
from ._sdl2 import lib, ffi
from .common import SdlRef, assert_zero, assert_nonnull

class Surface:
    def __init__(self, ref: SdlRef):
        self._ref = ref
        self._raw = ref._raw
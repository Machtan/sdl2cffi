from ._sdl2 import lib, ffi
from typing import Callable, Any, Optional

_sdl_allocated_objects = set()

class Allocated:
    """An abstract class for objects holding pointers to SDL2 objects that
    must be freed with a function."""
    __destroyed = False
    # TODO: How do I annotate this for mypy?
    _raw = None # type: Any
    def __init__(self, free_function: Callable[[Any], None]) -> None:
        _sdl_allocated_objects.add(self)
        self.__free_function = free_function
    
    def destroy(self):
        if not self.__destroyed and self._raw is not None:
            #print("{} freed!".format(type(self)))
            self.__free_function(self._raw)
            self.__destroyed = True
            _sdl_allocated_objects.remove(self)
    
    def __del__(self):
        self.destroy()

def get_error():
    return str(ffi.string(lib.SDL_GetError()), encoding="utf8")

class SDLError(Exception):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

def assert_zero(result):
    if result != 0:
        raise SDLError(get_error())
    return result

def assert_nonzero(result):
    if result == 0:
        raise SDLError(get_error())
    return result

def assert_nonnull(result):
    if result == ffi.NULL:
        raise SDLError(get_error())
    return result
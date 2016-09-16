from ._sdl2 import lib, ffi

_sdl_allocated_objects = set()

def Allocated(free_function):
    class Allocated:
        __destroyed = False
        def __init__(self):
            _sdl_allocated_objects.add(self)
        
        def destroy(self):
            if not self.__destroyed:
                print("{} freed!".format(type(self)))
                free_function(self._raw)
                self.__destroyed = True
                _sdl_allocated_objects.remove(self)
        
        def __del__(self):
            self.destroy()
    
    return Allocated

def get_error():
    return str(ffi.string(lib.SDL_GetError()), encoding="utf8")

class SDLError(Exception):
    def __init__(self, *args, **kwargs):
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
from _sdl2 import lib, ffi

def SDLAllocated(free_function):
    class SDLAllocated:
        __destroyed = False
        
        def destroy(self):
            if not self.__destroyed:
                print("{} freed!".format(type(self)))
                free_function(self._raw)
                self.__destroyed = True
        
        def __del__(self):
            self.destroy()
    
    return SDLAllocated

def get_error():
    return str(ffi.string(lib.SDL_GetError()), encoding="utf8")

class SDLError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **gwargs)

def assert_zero(result):
    if result != 0:
        raise SDLError(get_error())
    return result

def assert_non_null(result):
    if result == ffi.NULL:
        raise SDLError(get_error())
    return result
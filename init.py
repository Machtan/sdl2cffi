from ._sdl2 import ffi, lib
from .common import assert_zero, sdl_allocated_objects

class Context:
    """A context to run an SDL game in.
    Handles initialization and deinitialization"""
    def __init__(self, flags, image_flags):
        self.flags = flags
        self.image_flags = image_flags
        
    def __enter__(self):
        print("SDL Init")
        assert_zero(lib.SDL_Init(self.flags))
        lib.IMG_Init(self.image_flags)
        assert_zero(lib.TTF_Init())
    
    def __exit__(self, *args):
        print("Deinitializing...")
        for obj in sdl_allocated_objects:
            obj.destroy()
        lib.TTF_Quit()
        lib.IMG_Quit()
        lib.SDL_Quit()
        print("SDL Quit")

def init_everything():
    """Initializes SDL with all its subsystems.
    Returns a context to run an SDL game in."""
    #lib.SDL_Init(lib.SDL_INIT_EVERYTHING)
    image_flags = lib.IMG_INIT_JPG | lib.IMG_INIT_PNG | lib.IMG_INIT_TIF | lib.IMG_INIT_WEBP
    return Context(lib.SDL_INIT_EVERYTHING, image_flags)

def init(events=False, video=False, audio=False, game_controller=False,
        haptic=False, joystick=False, timer=False):
    """Initializes SDL with the given subsystems active.
    Returns a context to run an SDL game in."""
    flags = 0
    if events:          flags |= lib.SDL_INIT_EVENTS
    if video:           flags |= lib.SDL_INIT_VIDEO
    if audio:           flags |= lib.SDL_INIT_AUDIO
    if game_controller: flags |= lib.SDL_INIT_GAMECONTROLLER
    if haptic:          flags |= lib.SDL_INIT_HAPTIC
    if joystick:        flags |= lib.SDL_INIT_JOYSTICK
    if timer:           flags |= lib.SDL_INIT_TIMER
    return Context(flags, 0)

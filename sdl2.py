from _sdl2 import ffi, lib

class SdlContext:
    """A context to run an SDL game in.
    Handles initialization and deinitialization"""
    def __init__(self, flags):
        self.flags = flags
        
    def __enter__(self):
        print("SDL Init")
        lib.SDL_Init(self.flags)
    
    def __exit__(self, *args):
        print("SDL Quit")
        lib.SDL_Quit()

def init_everything():
    """Initializes SDL with all its subsystems.
    Returns a context to run an SDL game in."""
    #lib.SDL_Init(lib.SDL_INIT_EVERYTHING)
    return SdlContext(lib.SDL_INIT_EVERYTHING)

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
    return SdlContext(flags)

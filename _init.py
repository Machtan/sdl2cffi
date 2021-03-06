from ._sdl2 import ffi, lib
from .common import assert_zero, assert_nonzero, _sdl_allocated_objects
from .events import _poll_event, Quit, Event
from .window import WindowBuilder
import sys as _sys
from typing import Callable, Iterator

class SafeQuit(Exception): pass

class Context:
    """A context to run an SDL game in.
    Handles initialization and deinitialization"""
    def __init__(self, flags, image_flags, mixer_flags):
        self.flags = flags
        self.image_flags = image_flags
        self.mixer_flags = mixer_flags
        self._quit_handler = lambda: False
        
    def __enter__(self):
        print("SDL Init")
        assert_zero(lib.SDL_Init(self.flags))
        assert_nonzero(lib.IMG_Init(self.image_flags))
        assert_nonzero(lib.Mix_Init(self.mixer_flags))
        assert_zero(lib.TTF_Init())
        return self
    
    def set_quit_handler(self, handler: Callable[[], bool]):
        """Sets a function to be called when the Quit event is fired.
        Unless the function returns 'True', the context deinitialized,
        and execution returns to after the 'with' statement"""
        self._quit_handler = handler

    def get_events(self) -> Iterator[Event]:
        """Iterates over all pending events and empties the queue"""
        event = _poll_event()
        while event != None:
            if type(event) == Quit:
                abort_shutdown = self._quit_handler()
                if abort_shutdown is not True:
                    raise SafeQuit()
                    
            yield event
            event = _poll_event()
    
    def build_window(self) -> WindowBuilder:
        """Starts building a window with a WindowBuilder"""
        return WindowBuilder()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Deinitializing...")
        for obj in list(_sdl_allocated_objects):
            obj.destroy()
        
        lib.TTF_Quit()
        lib.Mix_Quit()
        lib.IMG_Quit()
        lib.SDL_Quit()
        
        print("SDL Quit")
        if exc_type == SafeQuit or exc_type == KeyboardInterrupt:
            return True

def init_everything() -> Context:
    """Initializes SDL with all its subsystems.
    Returns a context to run an SDL game in."""
    image_flags = (lib.IMG_INIT_JPG | lib.IMG_INIT_PNG | 
        lib.IMG_INIT_TIF | lib.IMG_INIT_WEBP)
    mixer_flags = (lib.MIX_INIT_FLAC | lib.MIX_INIT_MOD | lib.MIX_INIT_MODPLUG |
        lib.MIX_INIT_MP3 | lib.MIX_INIT_OGG | lib.MIX_INIT_FLUIDSYNTH)
    return Context(lib.SDL_INIT_EVERYTHING, image_flags, mixer_flags)

def init(events=False, video=False, audio=False, game_controller=False,
        haptic=False, joystick=False, timer=False) -> Context:
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
    return Context(flags, 0, 0)

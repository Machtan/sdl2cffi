from _sdl2 import ffi, lib

class Quit:
    """An event signaling that the application should quit"""
    def __init__(self, raw):
        self.timestamp = raw.timestamp

class Unhandled:
    def __init__(self, raw):
        self.raw = raw
    
    def __str__(self):
        return "Event(type: {}, {})".format(self.raw.type, self.raw)

def poll_event():
    event = ffi.new("SDL_Event*")
    res = lib.SDL_PollEvent(event)
    if res == 0:
        return None
    
    etype = event.type
    if etype == lib.SDL_KEYDOWN:
        print("KEY DOWN!")
    elif etype == lib.SDL_KEYUP:
        print("KEY UP!")
    elif etype == lib.SDL_MOUSEMOTION:
        print("MOUSE MOVED!")
    elif etype == lib.SDL_QUIT:
        return Quit(event.quit)
    
    return Unhandled(event)

def get_events():
    event = poll_event()
    while event != None:
        yield event
        event = poll_event()
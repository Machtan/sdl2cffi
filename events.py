from _sdl2 import ffi, lib

class TextEditing:
    def __init__(self, union):
        self.length = union.length
        self.start = union.start
        self.text = union.text
        self.timestamp = union.timestamp
        self.windowID = union.windowID

class MouseMotion:
    def __init__(self, union):
        self.state = union.state
        self.timestamp = union.timestamp
        self.which = union.which
        self.windowID = union.windowID
        self.x = union.x
        self.xrel = union.xrel
        self.y = union.y
        self.yrel = union.yrel

class UserEvent:
    def __init__(self, union):
        print('==== UserEvent ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class ControllerDeviceAdded:
    def __init__(self, union):
        print('==== ControllerDeviceAdded ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class KeymapChanged:
    pass

class FingerMotion:
    def __init__(self, union):
        self.dx = union.dx
        self.dy = union.dy
        self.fingerId = union.fingerId
        self.pressure = union.pressure
        self.timestamp = union.timestamp
        self.touchId = union.touchId
        self.x = union.x
        self.y = union.y

class DollarRecord:
    def __init__(self, union):
        print('==== DollarRecord ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class Joydeviceadded:
    def __init__(self, union):
        print('==== Joydeviceadded ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class ClipboardUpdate:
    pass

class KeyDown:
    def __init__(self, union):
        self.keysym = union.keysym
        self.padding2 = union.padding2
        self.padding3 = union.padding3
        self.repeat = union.repeat
        self.state = union.state
        self.timestamp = union.timestamp
        self.windowID = union.windowID

class Firstevent:
    def __init__(self, union):
        print('==== Firstevent ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class AppTerminating:
    pass

class SysWMEvent:
    def __init__(self, union):
        print('==== SysWMEvent ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class MouseButtonUp:
    def __init__(self, union):
        print('==== MouseButtonUp ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class ControllerButtonDown:
    def __init__(self, union):
        print('==== ControllerButtonDown ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class AppDidEnterForeground:
    pass

class WindowEvent:
    def __init__(self, union):
        self.data1 = union.data1
        self.data2 = union.data2
        self.event = union.event
        self.padding1 = union.padding1
        self.padding2 = union.padding2
        self.padding3 = union.padding3
        self.timestamp = union.timestamp
        self.windowID = union.windowID

class AudioDeviceAdded:
    def __init__(self, union):
        self.iscapture = union.iscapture
        self.padding1 = union.padding1
        self.padding2 = union.padding2
        self.padding3 = union.padding3
        self.timestamp = union.timestamp
        self.which = union.which

class Quit:
    def __init__(self, union):
        self.timestamp = union.timestamp

class ControllerDeviceRemoved:
    def __init__(self, union):
        print('==== ControllerDeviceRemoved ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class AppWillEnterBackground:
    pass

class JoyButtonUp:
    def __init__(self, union):
        print('==== JoyButtonUp ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class JoyBallMotion:
    def __init__(self, union):
        print('==== JoyBallMotion ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class AppWillEnterForeground:
    pass

class ControllerDeviceRemapped:
    def __init__(self, union):
        print('==== ControllerDeviceRemapped ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class MultiGesture:
    def __init__(self, union):
        self.dDist = union.dDist
        self.dTheta = union.dTheta
        self.numFingers = union.numFingers
        self.padding = union.padding
        self.timestamp = union.timestamp
        self.touchId = union.touchId
        self.x = union.x
        self.y = union.y

class Controllerbuttonup:
    def __init__(self, union):
        print('==== Controllerbuttonup ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class AppDidenterbackground:
    pass

class MouseWheel:
    def __init__(self, union):
        print('==== MouseWheel ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class Joydeviceremoved:
    def __init__(self, union):
        print('==== Joydeviceremoved ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class FingerUp:
    def __init__(self, union):
        self.dx = union.dx
        self.dy = union.dy
        self.fingerId = union.fingerId
        self.pressure = union.pressure
        self.timestamp = union.timestamp
        self.touchId = union.touchId
        self.x = union.x
        self.y = union.y

class Lastevent:
    pass

class TextInput:
    def __init__(self, union):
        self.text = union.text
        self.timestamp = union.timestamp
        self.windowID = union.windowID

class KeyUp:
    def __init__(self, union):
        self.keysym = union.keysym
        self.padding2 = union.padding2
        self.padding3 = union.padding3
        self.repeat = union.repeat
        self.state = union.state
        self.timestamp = union.timestamp
        self.windowID = union.windowID        

class RenderDeviceReset:
    pass

class Mousebuttondown:
    def __init__(self, union):
        print('==== Mousebuttondown ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class RenderTargetsReset:
    pass

class Joybuttondown:
    def __init__(self, union):
        print('==== Joybuttondown ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class Joyaxismotion:
    def __init__(self, union):
        print('==== Joyaxismotion ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class Dollargesture:
    def __init__(self, union):
        print('==== Dollargesture ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class FingerDown:
    def __init__(self, union):
        self.dx = union.dx
        self.dy = union.dy
        self.fingerId = union.fingerId
        self.pressure = union.pressure
        self.timestamp = union.timestamp
        self.touchId = union.touchId
        self.x = union.x
        self.y = union.y

class AppLowmemory:
    pass

class Audiodeviceremoved:
    def __init__(self, union):
        print('==== Audiodeviceremoved ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class Controlleraxismotion:
    def __init__(self, union):
        print('==== Controlleraxismotion ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class Joyhatmotion:
    def __init__(self, union):
        print('==== Joyhatmotion ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class Dropfile:
    def __init__(self, union):
        print('==== Dropfile ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

def _wrap_event(union):
    if union.type == lib.SDL_TEXTEDITING:
        return TextEditing(union.edit)
    elif union.type == lib.SDL_MOUSEMOTION:
        return MouseMotion(union.motion)
    elif union.type == lib.SDL_USEREVENT:
        return UserEvent(union.user)
    elif union.type == lib.SDL_CONTROLLERDEVICEADDED:
        return ControllerDeviceAdded(union.cdevice)
    elif union.type == lib.SDL_KEYMAPCHANGED:
        return KeymapChanged()
    elif union.type == lib.SDL_FINGERMOTION:
        return FingerMotion(union.tfinger)
    elif union.type == lib.SDL_DOLLARRECORD:
        return DollarRecord(union.dgesture)
    elif union.type == lib.SDL_JOYDEVICEADDED:
        return Joydeviceadded(union.jdevice)
    elif union.type == lib.SDL_CLIPBOARDUPDATE:
        return ClipboardUpdate()
    elif union.type == lib.SDL_KEYDOWN:
        return KeyDown(union.key)
    elif union.type == lib.SDL_FIRSTEVENT:
        return Firstevent(union.first)
    elif union.type == lib.SDL_APP_TERMINATING:
        return AppTerminating()
    elif union.type == lib.SDL_SYSWMEVENT:
        return SysWMEvent(union.syswm)
    elif union.type == lib.SDL_MOUSEBUTTONUP:
        return MouseButtonUp(union.button)
    elif union.type == lib.SDL_CONTROLLERBUTTONDOWN:
        return ControllerButtonDown(union.cbutton)
    elif union.type == lib.SDL_APP_DIDENTERFOREGROUND:
        return AppDidEnterForeground()
    elif union.type == lib.SDL_WINDOWEVENT:
        return WindowEvent(union.window)
    elif union.type == lib.SDL_AUDIODEVICEADDED:
        return AudioDeviceAdded(union.adevice)
    elif union.type == lib.SDL_QUIT:
        return Quit(union.quit)
    elif union.type == lib.SDL_CONTROLLERDEVICEREMOVED:
        return ControllerDeviceRemoved(union.cdevice)
    elif union.type == lib.SDL_APP_WILLENTERBACKGROUND:
        return AppWillEnterBackground()
    elif union.type == lib.SDL_JOYBUTTONUP:
        return JoyButtonUp(union.jbutton)
    elif union.type == lib.SDL_JOYBALLMOTION:
        return JoyBallMotion(union.jball)
    elif union.type == lib.SDL_APP_WILLENTERFOREGROUND:
        return AppWillEnterForeground()
    elif union.type == lib.SDL_CONTROLLERDEVICEREMAPPED:
        return ControllerDeviceRemapped(union.cdevice)
    elif union.type == lib.SDL_MULTIGESTURE:
        return MultiGesture(union.mgesture)
    elif union.type == lib.SDL_CONTROLLERBUTTONUP:
        return Controllerbuttonup(union.cbutton)
    elif union.type == lib.SDL_APP_DIDENTERBACKGROUND:
        return AppDidenterbackground()
    elif union.type == lib.SDL_MOUSEWHEEL:
        return MouseWheel(union.wheel)
    elif union.type == lib.SDL_JOYDEVICEREMOVED:
        return Joydeviceremoved(union.jdevice)
    elif union.type == lib.SDL_FINGERUP:
        return FingerUp(union.tfinger)
    elif union.type == lib.SDL_LASTEVENT:
        return Lastevent()
    elif union.type == lib.SDL_TEXTINPUT:
        return TextInput(union.text)
    elif union.type == lib.SDL_KEYUP:
        return KeyUp(union.key)
    elif union.type == lib.SDL_RENDER_DEVICE_RESET:
        return RenderDeviceReset()
    elif union.type == lib.SDL_MOUSEBUTTONDOWN:
        return Mousebuttondown(union.button)
    elif union.type == lib.SDL_RENDER_TARGETS_RESET:
        return RenderTargetsReset()
    elif union.type == lib.SDL_JOYBUTTONDOWN:
        return Joybuttondown(union.jbutton)
    elif union.type == lib.SDL_JOYAXISMOTION:
        return Joyaxismotion(union.jaxis)
    elif union.type == lib.SDL_DOLLARGESTURE:
        return Dollargesture(union.dgesture)
    elif union.type == lib.SDL_FINGERDOWN:
        return FingerDown(union.tfinger)
    elif union.type == lib.SDL_APP_LOWMEMORY:
        return AppLowmemory()
    elif union.type == lib.SDL_AUDIODEVICEREMOVED:
        return Audiodeviceremoved(union.adevice)
    elif union.type == lib.SDL_CONTROLLERAXISMOTION:
        return Controlleraxismotion(union.caxis)
    elif union.type == lib.SDL_JOYHATMOTION:
        return Joyhatmotion(union.jhat)
    elif union.type == lib.SDL_DROPFILE:
        return Dropfile(union.drop)
    else:
        raise Exception('Unreachable')

def poll_event():
    event = ffi.new("SDL_Event*")
    res = lib.SDL_PollEvent(event)
    if res == 0:
        return None
    
    return _wrap_event(event)

def get_events():
    event = poll_event()
    while event != None:
        yield event
        event = poll_event()
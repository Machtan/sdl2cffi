from ._sdl2 import ffi, lib
from keyboard import KeyMod
import sys as _sys

# ============ Notification events =================

class AppWillEnterForeground:
    pass

class AppDidEnterForeground:
    pass

class AppWillEnterBackground:
    pass

class AppDidEnterBackground:
    pass

class AppLowMemory:
    pass
    
class AppTerminating:
    pass

class KeymapChanged:
    pass

class ClipboardUpdate:
    pass

class RenderDeviceReset:
    pass

class RenderTargetsReset:
    pass

class AudioDeviceAdded:
    def __init__(self, union):
        self.iscapture = union.iscapture
        self.timestamp = union.timestamp
        self.which = union.which

class AudioDeviceRemoved:
    def __init__(self, union):
        print('==== AudioDeviceRemoved ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class Quit:
    def __init__(self, union):
        self.timestamp = union.timestamp

class UserEvent:
    def __init__(self, union):
        print('==== UserEvent ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

# ================= Window events ==================

class DropFile:
    def __init__(self, union):
        self.file = union.file
        self.timestamp = union.timestamp

class SysWMEvent:
    def __init__(self, union):
        print('==== SysWMEvent ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class WindowEvent:
    def __init__(self, union):
        self.data1 = union.data1
        self.data2 = union.data2
        self.event = union.event
        self.timestamp = union.timestamp
        self.windowID = union.windowID

# ================== Text events ====================

class TextInput:
    def __init__(self, union):
        self.text = union.text
        self.timestamp = union.timestamp
        self.windowID = union.windowID  

class TextEditing:
    def __init__(self, union):
        self.length = union.length
        self.start = union.start
        self.text = union.text
        self.timestamp = union.timestamp
        self.windowID = union.windowID

# ================== Mouse events ====================

class MouseButtonDown:
    def __init__(self, union):
        self.button = union.button
        self.clicks = union.clicks
        self.timestamp = union.timestamp
        self.state = union.state
        self.which = union.which
        self.windowID = union.windowID
        self.x = union.x
        self.y = union.y

class MouseButtonUp(MouseButtonDown):
    pass

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

class MouseWheel:
    def __init__(self, union):
        print('==== MouseWheel ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

# ================= Keyboard events ===================

class KeyDown:
    def __init__(self, union):
        self.scancode = union.keysym.scancode
        self.keycode = union.keysym.sym
        self.modifier_flags = union.keysym.mod
        self.repeat = union.repeat
        self.state = union.state
        self.timestamp = union.timestamp
        self.windowID = union.windowID
    
    def shortcut(self):
        if _sys.platform() == "darwin":
            return self.cmd()
        else:
            return self.ctrl()
    
    def ctrl(self):
        return (self.modifier_flags & (KeyMod.RCtrl | KeyMod.LCtrl)) != 0
    
    def gui(self):
        return (self.modifier_flags & (KeyMod.RGui | KeyMod.LGui)) != 0
    
    def shift(self):
        return (self.modifier_flags & (KeyMod.RShift | KeyMod.LShift)) != 0
    
    def alt(self):
        return (self.modifier_flags & (KeyMod.RAlt | KeyMod.LAlt)) != 0
    
    def cmd(self):
        return self.gui()
    
    def windows(self):
        return self.gui()

class KeyUp(KeyDown):
    pass

# ================== Touch events =====================

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

class FingerUp(FingerDown):
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

class DollarGesture:
    def __init__(self, union):
        print('==== DollarGesture ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class MultiGesture:
    def __init__(self, union):
        self.dDist = union.dDist
        self.dTheta = union.dTheta
        self.numFingers = union.numFingers
        self.timestamp = union.timestamp
        self.touchId = union.touchId
        self.x = union.x
        self.y = union.y

# ================== Joystick events =======================

class JoyDeviceAdded:
    def __init__(self, union):
        print('==== JoyDeviceAdded ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class JoyDeviceRemoved:
    def __init__(self, union):
        print('==== JoyDeviceRemoved ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class JoyButtonDown:
    def __init__(self, union):
        print('==== JoyButtonDown ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

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

class JoyHatMotion:
    def __init__(self, union):
        print('==== JoyHatMotion ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class JoyAxisMotion:
    def __init__(self, union):
        print('==== JoyAxisMotion ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

# ================== Controller events =====================

class ControllerDeviceAdded:
    def __init__(self, union):
        print('==== ControllerDeviceAdded ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class ControllerDeviceRemapped:
    def __init__(self, union):
        print('==== ControllerDeviceRemapped ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))
        
class ControllerDeviceRemoved:
    def __init__(self, union):
        print('==== ControllerDeviceRemoved ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class ControllerButtonDown:
    def __init__(self, union):
        print('==== ControllerButtonDown ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class ControllerButtonUp:
    def __init__(self, union):
        print('==== ControllerButtonUp ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class ControllerAxisMotion:
    def __init__(self, union):
        print('==== ControllerAxisMotion ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

# =================== Unused events =========================

class Firstevent:
    def __init__(self, union):
        print('==== Firstevent ====')
        for member in dir(union):
            if member == 'type': continue
            print('self.{} = union.{}'.format(member, member))

class Lastevent:
    pass


# ================== Functions ==============================

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
        return JoyDeviceAdded(union.jdevice)
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
        return ControllerButtonUp(union.cbutton)
    elif union.type == lib.SDL_APP_DIDENTERBACKGROUND:
        return AppDidEnterBackground()
    elif union.type == lib.SDL_MOUSEWHEEL:
        return MouseWheel(union.wheel)
    elif union.type == lib.SDL_JOYDEVICEREMOVED:
        return JoyDeviceRemoved(union.jdevice)
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
        return MouseButtonDown(union.button)
    elif union.type == lib.SDL_RENDER_TARGETS_RESET:
        return RenderTargetsReset()
    elif union.type == lib.SDL_JOYBUTTONDOWN:
        return JoyButtonDown(union.jbutton)
    elif union.type == lib.SDL_JOYAXISMOTION:
        return JoyAxisMotion(union.jaxis)
    elif union.type == lib.SDL_DOLLARGESTURE:
        return DollarGesture(union.dgesture)
    elif union.type == lib.SDL_FINGERDOWN:
        return FingerDown(union.tfinger)
    elif union.type == lib.SDL_APP_LOWMEMORY:
        return AppLowMemory()
    elif union.type == lib.SDL_AUDIODEVICEREMOVED:
        return AudioDeviceRemoved(union.adevice)
    elif union.type == lib.SDL_CONTROLLERAXISMOTION:
        return ControllerAxisMotion(union.caxis)
    elif union.type == lib.SDL_JOYHATMOTION:
        return JoyHatMotion(union.jhat)
    elif union.type == lib.SDL_DROPFILE:
        return DropFile(union.drop)
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
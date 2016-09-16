from _sdl2 import lib, ffi

class KeyMod:
    None_ = lib.KMOD_NONE
    LShift = lib.KMOD_LSHIFT
    RShift = lib.KMOD_RSHIFT
    LCtrl = lib.KMOD_LCTRL
    RCtrl = lib.KMOD_RCTRL
    LAlt = lib.KMOD_LALT
    RAlt = lib.KMOD_RALT
    LGui = lib.KMOD_LGUI
    RGui = lib.KMOD_RGUI
    NumLock = lib.KMOD_NUM
    CapsLock = lib.KMOD_CAPS
    AltGr = lib.KMOD_MODE
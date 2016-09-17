import os
import sys
import re
import pprint
from collections import OrderedDict
from _sdl2 import lib, ffi

from setup.fix_enums import find_enums

def printi(indent, msg, *args, **kwargs):
    print(indent*4*" "+msg, *args, **kwargs)

def load_enums():
    with open("setup/fixed_enums.h") as f:
        text = f.read()
    raw_enums = find_enums(text)
    enums = {}
    for enum in raw_enums:
        if enum.typedef is not None:
            members = OrderedDict()
            def sortkey(val):
                #print("Val: {}".format(val))
                return eval(val[1])
            
            for k, v in sorted(enum.members.items(), key=sortkey):
                members[k] = v
            
            enums[enum.typedef] = members

    return OrderedDict(sorted([(k, v) for k, v in enums.items()]))

def print_enums():
    for k in load_enums():
        print(k)
    
def print_member_list(enum_name):
    print(load_enums().get(enum_name))

def longest_name(iterable):
    maxlen = 0
    maxname = None
    for name in iterable:
        if len(name) > maxlen:
            maxlen = len(name)
            maxname = name
    return maxname

def print_enum_map(enum_name, prefix=""):
    members = load_enums().get(enum_name)
    #print("enum: {}".format(enum))
    #print(load_enums())
    longest = longest_name(members.keys())
    if members is None:
        raise Exception("Enum {!r} not found!".format(enum_name))
    print("values = {")
    for member in members:
        pad = (len(longest) - len(member)) * " "
        print("    \"{}{}\": {},".format(prefix, member, pad))
    print("}")

EVENT_MEMBER_MAP = {
    "lib.SDL_FIRSTEVENT":               "first",
    "lib.SDL_QUIT":                     "quit",
    "lib.SDL_APP_TERMINATING":          "",
    "lib.SDL_APP_LOWMEMORY":            "",
    "lib.SDL_APP_WILLENTERBACKGROUND":  "",
    "lib.SDL_APP_DIDENTERBACKGROUND":   "",
    "lib.SDL_APP_WILLENTERFOREGROUND":  "",
    "lib.SDL_APP_DIDENTERFOREGROUND":   "",
    "lib.SDL_WINDOWEVENT":              "window",
    "lib.SDL_SYSWMEVENT":               "syswm",
    "lib.SDL_KEYDOWN":                  "key",
    "lib.SDL_KEYUP":                    "key",
    "lib.SDL_TEXTEDITING":              "edit",
    "lib.SDL_TEXTINPUT":                "text",
    "lib.SDL_KEYMAPCHANGED":            "",
    "lib.SDL_MOUSEMOTION":              "motion",
    "lib.SDL_MOUSEBUTTONDOWN":          "button",
    "lib.SDL_MOUSEBUTTONUP":            "button",
    "lib.SDL_MOUSEWHEEL":               "wheel",
    "lib.SDL_JOYAXISMOTION":            "jaxis",
    "lib.SDL_JOYBALLMOTION":            "jball",
    "lib.SDL_JOYHATMOTION":             "jhat",
    "lib.SDL_JOYBUTTONDOWN":            "jbutton",
    "lib.SDL_JOYBUTTONUP":              "jbutton",
    "lib.SDL_JOYDEVICEADDED":           "jdevice",
    "lib.SDL_JOYDEVICEREMOVED":         "jdevice",
    "lib.SDL_CONTROLLERAXISMOTION":     "caxis",
    "lib.SDL_CONTROLLERBUTTONDOWN":     "cbutton",
    "lib.SDL_CONTROLLERBUTTONUP":       "cbutton",
    "lib.SDL_CONTROLLERDEVICEADDED":    "cdevice",
    "lib.SDL_CONTROLLERDEVICEREMOVED":  "cdevice",
    "lib.SDL_CONTROLLERDEVICEREMAPPED": "cdevice",
    "lib.SDL_FINGERDOWN":               "tfinger",
    "lib.SDL_FINGERUP":                 "tfinger",
    "lib.SDL_FINGERMOTION":             "tfinger",
    "lib.SDL_DOLLARGESTURE":            "dgesture",
    "lib.SDL_DOLLARRECORD":             "dgesture",
    "lib.SDL_MULTIGESTURE":             "mgesture",
    "lib.SDL_CLIPBOARDUPDATE":          "",
    "lib.SDL_DROPFILE":                 "drop",
    "lib.SDL_AUDIODEVICEADDED":         "adevice",
    "lib.SDL_AUDIODEVICEREMOVED":       "adevice",
    "lib.SDL_RENDER_TARGETS_RESET":     "",
    "lib.SDL_RENDER_DEVICE_RESET":      "",
    "lib.SDL_USEREVENT":                "user",
    "lib.SDL_LASTEVENT":                "",
}
def generate_union_wrappers(func_name, type_member, const_prefix, member_map):
    cnames = {}
    for value, member in member_map.items():
        const = value.split(const_prefix, 1)[1]
        cname = "".join([p.capitalize() for p in const.split("_")])
        print("class {}:".format(cname))
        if member == "":
            printi(1, "pass\n")
            cnames[value] = cname
            continue
        printi(1, "def __init__(self, union):")
        printi(2, "print('==== {} ====')".format(cname))
        printi(2, "for member in dir(union):")
        printi(3, "if member == '{}': continue".format(type_member))
        printi(3, "print('self.{} = union.{}'.format(member, member))")
        print("")
        cnames[value] = cname
    print("def {}(union):".format(func_name))
    for i, (value, member) in enumerate(member_map.items()):
        prefix = "" if i == 0 else "el"
        printi(1, "{}if union.{} == {}:".format(prefix, type_member, value))
        if member == "":
            printi(2, "return {}()".format(cnames[value]))
        else:
            printi(2, "return {}(union.{})".format(cnames[value], member))
    printi(1, "else:")
    printi(2, "raise Exception('Unreachable')")

def wrap_enum(lib, name, prefix):
    members = [v for v in dir(lib) if v.startswith(prefix)]
    fixed = ["".join([p.capitalize() for p in mem[len(prefix):].split("_")]) for mem in members]
    print("class {}:".format(name))
    longest = longest_name(fixed)
    for i in range(len(members)):
        mem, fix = members[i], fixed[i] 
        pad = (len(longest) - len(fix)) * " "
        printi(1, "{}{} = lib.{}".format(fix, pad, mem))

def main():
    wrap_enum(lib, "Scancode", "SDL_SCANCODE_")

if __name__ == '__main__':
    main()

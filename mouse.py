from _sdl2 import lib, ffi

class MouseButton:
    Left = lib.SDL_BUTTON_LEFT
    Middle = lib.SDL_BUTTON_MIDDLE
    Right = lib.SDL_BUTTON_RIGHT
    X1 = lib.SDL_BUTTON_X1
    X2 = lib.SDL_BUTTON_X2
    
    def name(button):
        if button == MouseButton.Left:
            return "Left"
        elif button == MouseButton.Middle:
            return "Middle"
        elif button == MouseButton.Right:
            return "Right"
        elif button == MouseButton.X1:
            return "X1"
        elif button == MouseButton.X2:
            return "X2"
        else:
            raise ValueError("Unknown mouse button value: '{}'".format(button))
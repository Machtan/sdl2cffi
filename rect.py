from ._sdl2 import lib, ffi

class Rect:
    def __init__(self, x, y, w, h):
        self._raw_ = ffi.new("SDL_Rect *", [x, y, w, h])
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    @property
    def _raw(self):
        self._raw_.x = self.x
        self._raw_.y = self.y
        self._raw_.w = self.w
        self._raw_.h = self.h
        return self._raw_
    
    @property
    def left(self):
        return self.x
    
    @left.setter
    def left(self, value):
        self.x = value
    
    @property
    def right(self):
        return self.x + self.w
    
    @right.setter
    def right(self, value):
        self.x = value - self.w
    
    @property
    def top(self):
        return self.y
    
    @top.setter
    def top(self, value):
        self.y = value
    
    @property
    def bottom(self):
        return self.y + self.h
    
    @bottom.setter
    def bottom(self, value):
        self.y = value - self.h
    
    def clone(self):
        return Rect(self.x, self.y, self.w, self.h)
    
    def center(self):
        return (self.x + self.w / 2, self.y + self.h / 2)
    
    def move_to(self, x, y):
        self.x = x
        self.y = y
        return self
    
    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy
        return self
    
    def center_on(self, x, y):
        self.x = x - self.w / 2
        self.y = y - self.h / 2
        return self
    
    def resize(self, w, h):
        self.w = w
        self.h = h
        return self
    
    def moved_to(self, x, y):
        return self.clone().move_to(x, y)
    
    def moved_by(self, dx, dy):
        return self.clone().move_by(dx, dy)
    
    def centered_on(self, x, y):
        return self.clone().center_on(x, y)
    
    def resized(self, w, h):
        return self.clone().resize(w, h)
        
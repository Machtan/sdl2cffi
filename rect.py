from ._sdl2 import lib, ffi

from typing import Tuple

class Rect:
    def __init__(self, x, y, w, h) -> None:
        self._raw_ = ffi.new("SDL_Rect *", [x, y, w, h])
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def from_points(x1, y1, x2, y2) -> 'Rect':
        x = min(x1, x2)
        w = max(x1, x2) - x
        y = min(y1, y2)
        h = max(y1, y2) - y
        return Rect(x, y, w, h)
    
    def from_center(center, size) -> 'Rect':
        cx, cy = center
        w, h = size
        x = int(round(cx - w / 2))
        y = int(round(cy - h / 2))
        return Rect(x, y, w, h)
    
    @property
    def _raw(self):
        self._raw_.x = self.x
        self._raw_.y = self.y
        self._raw_.w = self.w
        self._raw_.h = self.h
        return self._raw_
    
    @property
    def left(self) -> int:
        return self.x
    
    @left.setter
    def left(self, value: int):
        self.x = value
    
    @property
    def right(self) -> int:
        return self.x + self.w
    
    @right.setter
    def right(self, value: int):
        self.x = value - self.w
    
    @property
    def top(self) -> int:
        return self.y
    
    @top.setter
    def top(self, value: int):
        self.y = value
    
    @property
    def bottom(self) -> int:
        return self.y + self.h
    
    @bottom.setter
    def bottom(self, value: int):
        self.y = value - self.h
    
    def clone(self) -> 'Rect':
        return Rect(self.x, self.y, self.w, self.h)
    
    def center(self) -> Tuple[int, int]:
        return (self.x + self.w // 2, self.y + self.h // 2)
    
    def move_to(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def move_by(self, dx: int, dy: int):
        self.x += dx
        self.y += dy
    
    def center_on(self, x: int, y: int):
        self.x = x - self.w / 2
        self.y = y - self.h / 2
    
    def resize(self, w: int, h: int):
        self.w = w
        self.h = h
    
    def include(self, x: int, y: int):
        """Resizes the rect to include the given point"""
        if x < self.x:
            self.w += self.x - x
            self.x = x
        elif x > self.right:
            self.w = x - self.x
        if y < self.y:
            self.h += self.y - y
            self.y = y
        elif y > self.bottom:
            self.h = y - self.y
    
    def moved_to(self, x: int, y: int) -> 'Rect':
        return Rect(x, y, self.w, self.h)
    
    def moved_by(self, dx: int, dy: int) -> 'Rect':
        return Rect(self.x + dx, self.y + dy, self.w, self.h)
    
    def centered_on(self, x, y) -> 'Rect':
        return Rect.from_center((x, y), (self.w, self.h))
    
    def resized(self, w, h) -> 'Rect':
        return Rect(self.x, self.y, w, h)
    
    def contains(self, x: int, y: int) -> bool:
        return x >= self.x and x <= self.right and y >= self.y and y <= self.bottom
        
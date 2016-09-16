from .init import init_everything, init, Context
from .window import WindowBuilder, Window
from .render import RendererBuilder, Renderer, Texture, EBlendMode, EFlip
from .events import get_events, poll_event
from .surface import Surface
from .rect import Rect
from .font import Font

from . import events
from . import keyboard

# Is this the right way?
del _sdl2
del common
del window
del render
del surface
del rect
del font
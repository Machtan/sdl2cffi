# What is this?
A python binding to version 2.0.4 of the SDL game development library.

# Requirements
**A \*nix OS**
**Python 3.x**
**cffi**
```pip install cffi```
**SDL2**
_OSX_
```brew install sdl2```
_Anything else_
Use your package manager :)

# Installation
run ```python3 setup/build.py <path to SDL.h>```
...
The wrapper isn't done yet, but you can ```import _sdl2``` to import the cffi bindings object and very inconveniently do stuff.
'''OpenGL extension EXT.swap_control_tear

This module customises the behaviour of the 
OpenGL.raw.WGL.EXT.swap_control_tear to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/swap_control_tear.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.WGL import _types
from OpenGL.raw.WGL.EXT.swap_control_tear import *
from OpenGL.raw.WGL.EXT.swap_control_tear import _EXTENSION_NAME

def glInitSwapControlTearEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
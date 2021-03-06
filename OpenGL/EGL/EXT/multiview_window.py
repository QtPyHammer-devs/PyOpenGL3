"""OpenGL extension EXT.multiview_window

This module customises the behaviour of the 
OpenGL.raw.EGL.EXT.multiview_window to provide a more 
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/EXT/multiview_window.txt
"""
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.EXT.multiview_window import *
from OpenGL.raw.EGL.EXT.multiview_window import _EXTENSION_NAME

def glInitMultiviewWindowEXT():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# END AUTOGENERATED SECTION
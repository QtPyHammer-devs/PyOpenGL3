'''OpenGL extension DFX.multisample

This module customises the behaviour of the 
OpenGL.raw.WGL.DFX.multisample to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/DFX/multisample.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.WGL import _types
from OpenGL.raw.WGL.DFX.multisample import *
from OpenGL.raw.WGL.DFX.multisample import _EXTENSION_NAME

def glInitMultisampleDFX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
'''OpenGL extension NV.copy_image

This module customises the behaviour of the 
OpenGL.raw.WGL.NV.copy_image to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/copy_image.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.WGL import _types
from OpenGL.raw.WGL.NV.copy_image import *
from OpenGL.raw.WGL.NV.copy_image import _EXTENSION_NAME

def glInitCopyImageNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
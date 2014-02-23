'''OpenGL extension SGI.cushion

This module customises the behaviour of the 
OpenGL.raw.GLX.SGI.cushion to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGI/cushion.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.SGI.cushion import *
from OpenGL.raw.GLX.SGI.cushion import _EXTENSION_NAME

def glInitCushionSGI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION
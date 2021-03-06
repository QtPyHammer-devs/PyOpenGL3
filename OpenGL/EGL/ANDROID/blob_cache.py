"""OpenGL extension ANDROID.blob_cache

This module customises the behaviour of the
OpenGL.raw.EGL.ANDROID.blob_cache to provide a more
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/ANDROID/blob_cache.txt"""
from OpenGL import extensions
from OpenGL.raw.EGL.ANDROIN.blob_cache import _EXTENSION_NAME


def glInitBlobCacheANDROID():
    """Return boolean indicating whether this extension is available"""
    return extensions.hasGLExtension(_EXTENSION_NAME)

# END AUTOGENERATED SECTION

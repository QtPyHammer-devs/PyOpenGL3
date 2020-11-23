"""OpenGL extension VERSION.GL_1_0

This module customises the behaviour of the
OpenGL.raw.GL.VERSION.GL_1_0 to provide a more
Python-friendly API

The official definition of this extension is available here:
https://www.opengl.org/registry/specs/VERSION/GL_1_0.txt"""
# load raw OpenGL functions for OpenGL 1.0
# from OpenGL.raw.GL.VERSION.GL_1_0 import *
from OpenGL.raw.GL.VERSION.GL_1_0 import _EXTENSION_NAME, _glgets, wrapper
import OpenGL.raw.GL.VERSION.GL_1_0 as raw


def glInitGl10VERSION():
    """Return boolean indicating whether this extension is available"""
    from OpenGL import extensions
    return extensions.hasGLExtension(_EXTENSION_NAME)


# INPUT glTexParameterfv.params size not checked against "pname"
glTexParameterfv = wrapper.wrapper(raw.glTexParameterfv).setInputArraySize("params", None)
# INPUT glTexParameteriv.params size not checked against "pname"
glTexParameteriv = wrapper.wrapper(raw.glTexParameteriv).setInputArraySize("params", None)
# INPUT glTexImage1D.pixels size not checked against "format, type, width"
glTexImage1D = wrapper.wrapper(raw.glTexImage1D).setInputArraySize("pixels", None)
# INPUT glTexImage2D.pixels size not checked against "format, type, width, height"
glTexImage2D = wrapper.wrapper(raw.glTexImage2D).setInputArraySize("pixels", None)
# OUTPUT glReadPixels.pixels COMPSIZE(format, type, width, height)
glGetBooleanv = wrapper.wrapper(raw.glGetBooleanv).setOutput(
    "data", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetDoublev = wrapper.wrapper(raw.glGetDoublev).setOutput(
    "data", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetFloatv = wrapper.wrapper(raw.glGetFloatv).setOutput(
    "data", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetIntegerv = wrapper.wrapper(raw.glGetIntegerv).setOutput(
    "data", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
# OUTPUT glGetTexImage.pixels COMPSIZE(target, level, format, type)
glGetTexParameterfv = wrapper.wrapper(raw.glGetTexParameterfv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetTexParameteriv = wrapper.wrapper(raw.glGetTexParameteriv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetTexLevelParameterfv = wrapper.wrapper(raw.glGetTexLevelParameterfv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetTexLevelParameteriv = wrapper.wrapper(raw.glGetTexLevelParameteriv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
# INPUT glCallLists.lists size not checked against "n,type"
glCallLists = wrapper.wrapper(raw.glCallLists).setInputArraySize("lists", None)
# INPUT glBitmap.bitmap size not checked against "width,height"
glBitmap = wrapper.wrapper(raw.glBitmap).setInputArraySize("bitmap", None)

glColor3bv = wrapper.wrapper(raw.glColor3bv).setInputArraySize("v", 3)
glColor3dv = wrapper.wrapper(raw.glColor3dv).setInputArraySize("v", 3)
glColor3fv = wrapper.wrapper(raw.glColor3fv).setInputArraySize("v", 3)
glColor3iv = wrapper.wrapper(raw.glColor3iv).setInputArraySize("v", 3)
glColor3sv = wrapper.wrapper(raw.glColor3sv).setInputArraySize("v", 3)
glColor3ubv = wrapper.wrapper(raw.glColor3ubv).setInputArraySize("v", 3)
glColor3uiv = wrapper.wrapper(raw.glColor3uiv).setInputArraySize("v", 3)
glColor3usv = wrapper.wrapper(raw.glColor3usv).setInputArraySize("v", 3)

glColor4bv = wrapper.wrapper(raw.glColor4bv).setInputArraySize("v", 4)
glColor4dv = wrapper.wrapper(raw.glColor4dv).setInputArraySize("v", 4)
glColor4fv = wrapper.wrapper(raw.glColor4fv).setInputArraySize("v", 4)
glColor4iv = wrapper.wrapper(raw.glColor4iv).setInputArraySize("v", 4)
glColor4sv = wrapper.wrapper(raw.glColor4sv).setInputArraySize("v", 4)
glColor4ubv = wrapper.wrapper(raw.glColor4ubv).setInputArraySize("v", 4)
glColor4uiv = wrapper.wrapper(raw.glColor4uiv).setInputArraySize("v", 4)
glColor4usv = wrapper.wrapper(raw.glColor4usv).setInputArraySize("v", 4)

glEdgeFlagv = wrapper.wrapper(raw.glEdgeFlagv).setInputArraySize("flag", 1)
glIndexdv = wrapper.wrapper(raw.glIndexdv).setInputArraySize("c", 1)
glIndexfv = wrapper.wrapper(raw.glIndexfv).setInputArraySize("c", 1)
glIndexiv = wrapper.wrapper(raw.glIndexiv).setInputArraySize("c", 1)
glIndexsv = wrapper.wrapper(raw.glIndexsv).setInputArraySize("c", 1)

glNormal3bv = wrapper.wrapper(raw.glNormal3bv).setInputArraySize("v", 3)
glNormal3dv = wrapper.wrapper(raw.glNormal3dv).setInputArraySize("v", 3)
glNormal3fv = wrapper.wrapper(raw.glNormal3fv).setInputArraySize("v", 3)
glNormal3iv = wrapper.wrapper(raw.glNormal3iv).setInputArraySize("v", 3)
glNormal3sv = wrapper.wrapper(raw.glNormal3sv).setInputArraySize("v", 3)

glRasterPos2dv = wrapper.wrapper(raw.glRasterPos2dv).setInputArraySize("v", 2)
glRasterPos2fv = wrapper.wrapper(raw.glRasterPos2fv).setInputArraySize("v", 2)
glRasterPos2iv = wrapper.wrapper(raw.glRasterPos2iv).setInputArraySize("v", 2)
glRasterPos2sv = wrapper.wrapper(raw.glRasterPos2sv).setInputArraySize("v", 2)
glRasterPos3dv = wrapper.wrapper(raw.glRasterPos3dv).setInputArraySize("v", 3)
glRasterPos3fv = wrapper.wrapper(raw.glRasterPos3fv).setInputArraySize("v", 3)
glRasterPos3iv = wrapper.wrapper(raw.glRasterPos3iv).setInputArraySize("v", 3)
glRasterPos3sv = wrapper.wrapper(raw.glRasterPos3sv).setInputArraySize("v", 3)

glRasterPos4dv = wrapper.wrapper(raw.glRasterPos4dv).setInputArraySize("v", 4)
glRasterPos4fv = wrapper.wrapper(raw.glRasterPos4fv).setInputArraySize("v", 4)
glRasterPos4iv = wrapper.wrapper(raw.glRasterPos4iv).setInputArraySize("v", 4)
glRasterPos4sv = wrapper.wrapper(raw.glRasterPos4sv).setInputArraySize("v", 4)

glRectdv = wrapper.wrapper(raw.glRectdv).setInputArraySize("v1", 2).setInputArraySize("v2", 2)
glRectfv = wrapper.wrapper(raw.glRectfv).setInputArraySize("v1", 2).setInputArraySize("v2", 2)
glRectiv = wrapper.wrapper(raw.glRectiv).setInputArraySize("v1", 2).setInputArraySize("v2", 2)
glRectsv = wrapper.wrapper(raw.glRectsv).setInputArraySize("v1", 2).setInputArraySize("v2", 2)

glTexCoord1dv = wrapper.wrapper(raw.glTexCoord1dv).setInputArraySize("v", 1)
glTexCoord1fv = wrapper.wrapper(raw.glTexCoord1fv).setInputArraySize("v", 1)
glTexCoord1iv = wrapper.wrapper(raw.glTexCoord1iv).setInputArraySize("v", 1)
glTexCoord1sv = wrapper.wrapper(raw.glTexCoord1sv).setInputArraySize("v", 1)

glTexCoord2dv = wrapper.wrapper(raw.glTexCoord2dv).setInputArraySize("v", 2)
glTexCoord2fv = wrapper.wrapper(raw.glTexCoord2fv).setInputArraySize("v", 2)
glTexCoord2iv = wrapper.wrapper(raw.glTexCoord2iv).setInputArraySize("v", 2)
glTexCoord2sv = wrapper.wrapper(raw.glTexCoord2sv).setInputArraySize("v", 2)

glTexCoord3dv = wrapper.wrapper(raw.glTexCoord3dv).setInputArraySize("v", 3)
glTexCoord3fv = wrapper.wrapper(raw.glTexCoord3fv).setInputArraySize("v", 3)
glTexCoord3iv = wrapper.wrapper(raw.glTexCoord3iv).setInputArraySize("v", 3)
glTexCoord3sv = wrapper.wrapper(raw.glTexCoord3sv).setInputArraySize("v", 3)

glTexCoord4dv = wrapper.wrapper(raw.glTexCoord4dv).setInputArraySize("v", 4)
glTexCoord4fv = wrapper.wrapper(raw.glTexCoord4fv).setInputArraySize("v", 4)
glTexCoord4iv = wrapper.wrapper(raw.glTexCoord4iv).setInputArraySize("v", 4)
glTexCoord4sv = wrapper.wrapper(raw.glTexCoord4sv).setInputArraySize("v", 4)

glVertex2dv = wrapper.wrapper(raw.glVertex2dv).setInputArraySize("v", 2)
glVertex2fv = wrapper.wrapper(raw.glVertex2fv).setInputArraySize("v", 2)
glVertex2iv = wrapper.wrapper(raw.glVertex2iv).setInputArraySize("v", 2)
glVertex2sv = wrapper.wrapper(raw.glVertex2sv).setInputArraySize("v", 2)

glVertex3dv = wrapper.wrapper(raw.glVertex3dv).setInputArraySize("v", 3)
glVertex3fv = wrapper.wrapper(raw.glVertex3fv).setInputArraySize("v", 3)
glVertex3iv = wrapper.wrapper(raw.glVertex3iv).setInputArraySize("v", 3)
glVertex3sv = wrapper.wrapper(raw.glVertex3sv).setInputArraySize("v", 3)

glVertex4dv = wrapper.wrapper(raw.glVertex4dv).setInputArraySize("v", 4)
glVertex4fv = wrapper.wrapper(raw.glVertex4fv).setInputArraySize("v", 4)
glVertex4iv = wrapper.wrapper(raw.glVertex4iv).setInputArraySize("v", 4)
glVertex4sv = wrapper.wrapper(raw.glVertex4sv).setInputArraySize("v", 4)

glClipPlane = wrapper.wrapper(raw.glClipPlane).setInputArraySize("equation", 4)

# INPUT glFogfv.params size not checked against "pname"
glFogfv = wrapper.wrapper(raw.glFogfv).setInputArraySize("params", None)
# INPUT glFogiv.params size not checked against "pname"
glFogiv = wrapper.wrapper(raw.glFogiv).setInputArraySize("params", None)
# INPUT glLightfv.params size not checked against "pname"
glLightfv = wrapper.wrapper(raw.glLightfv).setInputArraySize("params", None)
# INPUT glLightiv.params size not checked against "pname"
glLightiv = wrapper.wrapper(raw.glLightiv).setInputArraySize("params", None)
# INPUT glLightModelfv.params size not checked against "pname"
glLightModelfv = wrapper.wrapper(raw.glLightModelfv).setInputArraySize("params", None)
# INPUT glLightModeliv.params size not checked against "pname"
glLightModeliv = wrapper.wrapper(raw.glLightModeliv).setInputArraySize("params", None)
# INPUT glMaterialfv.params size not checked against "pname"
glMaterialfv = wrapper.wrapper(raw.glMaterialfv).setInputArraySize("params", None)
# INPUT glMaterialiv.params size not checked against "pname"
glMaterialiv = wrapper.wrapper(raw.glMaterialiv).setInputArraySize("params", None)
# INPUT glPolygonStipple.mask size not checked against ""
glPolygonStipple = wrapper.wrapper(raw.glPolygonStipple).setInputArraySize("mask", None)
# INPUT glTexEnvfv.params size not checked against "pname"
glTexEnvfv = wrapper.wrapper(raw.glTexEnvfv).setInputArraySize("params", None)
# INPUT glTexEnviv.params size not checked against "pname"
glTexEnviv = wrapper.wrapper(raw.glTexEnviv).setInputArraySize("params", None)
# INPUT glTexGendv.params size not checked against "pname"
glTexGendv = wrapper.wrapper(raw.glTexGendv).setInputArraySize("params", None)
# INPUT glTexGenfv.params size not checked against "pname"
glTexGenfv = wrapper.wrapper(raw.glTexGenfv).setInputArraySize("params", None)
# INPUT glTexGeniv.params size not checked against "pname"
glTexGeniv = wrapper.wrapper(raw.glTexGeniv).setInputArraySize("params", None)

glFeedbackBuffer = wrapper.wrapper(raw.glFeedbackBuffer).setOutput(
    "buffer", size=lambda x:(x,), pnameArg="size", orPassIn=True)
glSelectBuffer = wrapper.wrapper(raw.glSelectBuffer).setOutput(
    "buffer", size=lambda x:(x,), pnameArg="size", orPassIn=True)

# INPUT glMap1d.points size not checked against "target, stride, order"
glMap1d = wrapper.wrapper(raw.glMap1d).setInputArraySize("points", None)
# INPUT glMap1f.points size not checked against "target,stride,order"
glMap1f = wrapper.wrapper(raw.glMap1f).setInputArraySize("points", None)
# INPUT glMap2d.points size not checked against "target, ustride, uorder, vstride, vorder"
glMap2d = wrapper.wrapper(raw.glMap2d).setInputArraySize("points", None)
# INPUT glMap2f.points size not checked against "target, ustride, uorder, vstride, vorder"
glMap2f = wrapper.wrapper(raw.glMap2f).setInputArraySize("points", None)

glEvalCoord1dv = wrapper.wrapper(raw.glEvalCoord1dv).setInputArraySize("u", 1)
glEvalCoord1fv = wrapper.wrapper(raw.glEvalCoord1fv).setInputArraySize("u", 1)

glEvalCoord2dv = wrapper.wrapper(raw.glEvalCoord2dv).setInputArraySize("u", 2)
glEvalCoord2fv = wrapper.wrapper(raw.glEvalCoord2fv).setInputArraySize("u", 2)

# INPUT glPixelMapfv.values size not checked against mapsize
glPixelMapfv = wrapper.wrapper(raw.glPixelMapfv).setInputArraySize("values", None)
# INPUT glPixelMapuiv.values size not checked against mapsize
glPixelMapuiv = wrapper.wrapper(raw.glPixelMapuiv).setInputArraySize("values", None)
# INPUT glPixelMapusv.values size not checked against mapsize
glPixelMapusv = wrapper.wrapper(raw.glPixelMapusv).setInputArraySize("values", None)
# INPUT glDrawPixels.pixels size not checked against "format,type,width,height"
glDrawPixels = wrapper.wrapper(raw.glDrawPixels).setInputArraySize("pixels", None)

glGetClipPlane = wrapper.wrapper(raw.glGetClipPlane).setOutput("equation", size=(4,), orPassIn=True)
glGetLightfv = wrapper.wrapper(raw.glGetLightfv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetLightiv = wrapper.wrapper(raw.glGetLightiv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
# OUTPUT glGetMapdv.v COMPSIZE(target, query)
# OUTPUT glGetMapfv.v COMPSIZE(target, query)
# OUTPUT glGetMapiv.v COMPSIZE(target, query)
glGetMaterialfv = wrapper.wrapper(raw.glGetMaterialfv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetMaterialiv = wrapper.wrapper(raw.glGetMaterialiv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetPixelMapfv = wrapper.wrapper(raw.glGetPixelMapfv).setOutput(
    "values", size=_glgets._glget_size_mapping, pnameArg="map", orPassIn=True)
glGetPixelMapuiv = wrapper.wrapper(raw.glGetPixelMapuiv).setOutput(
    "values", size=_glgets._glget_size_mapping, pnameArg="map", orPassIn=True)
glGetPixelMapusv = wrapper.wrapper(raw.glGetPixelMapusv).setOutput(
    "values", size=_glgets._glget_size_mapping, pnameArg="map", orPassIn=True)
glGetPolygonStipple = wrapper.wrapper(raw.glGetPolygonStipple).setOutput(
    "mask", size=lambda x: (x,), pnameArg="128.0", orPassIn=True)
glGetTexEnvfv = wrapper.wrapper(raw.glGetTexEnvfv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetTexEnviv = wrapper.wrapper(raw.glGetTexEnviv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetTexGendv = wrapper.wrapper(raw.glGetTexGendv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetTexGenfv = wrapper.wrapper(raw.glGetTexGenfv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)
glGetTexGeniv = wrapper.wrapper(raw.glGetTexGeniv).setOutput(
    "params", size=_glgets._glget_size_mapping, pnameArg="pname", orPassIn=True)

glLoadMatrixf = wrapper.wrapper(raw.glLoadMatrixf).setInputArraySize("m", 16)
glLoadMatrixd = wrapper.wrapper(raw.glLoadMatrixd).setInputArraySize("m", 16)
glMultMatrixf = wrapper.wrapper(raw.glMultMatrixf).setInputArraySize("m", 16)
glMultMatrixd = wrapper.wrapper(raw.glMultMatrixd).setInputArraySize("m", 16)

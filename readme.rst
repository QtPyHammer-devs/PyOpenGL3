Goals of this fork
================
To update the entire PyOpenGL binding to Python 3.8+

This will include use of f-strings, type hints & removing Python 2.7 support where readbility can be improved

To generate docstrings from either text files or https://www.khronos.org/registry/OpenGL-Refpages/gl4/html on install  

(This repo is huge so automating changes will be very important)

To inform the programmer of errors in a way that is instructive & state aware, while retaining C OpenGL error codes

Catch errors the OpenGL C implementation communicates poorly (non-square cubemap texture etc.)

To remove the need for numpy, with quick the translation of python types into bytes handled invisibly::

    $ function(GL_FLOAT, iterable)

Before being passed to C, translate iterable to bytestring, taking hints from other arguments  
<<<<<<< HEAD
  
PyOpenGL and PyOpenGL_accelerate
=================================

PyOpenGL is normally distributed via PyPI using standard pip::

    $ pip install PyOpenGL PyOpenGL_accelerate

You can install this repository by branching/cloning and running
setup.py::

    $ cd pyopengl
    $ python setup.py develop
    $ cd accelerate
    $ python setup.py develop

Note that to compile PyOpenGL_accelerate you will need to have
a functioning Python extension-compiling environment.

Learning PyOpenGL
-----------------

If you are new to PyOpenGL, you likely want to start with the OpenGLContext `tutorial page`_.
Those tutorials require OpenGLContext, (which is a big wrapper including a whole
scenegraph engine, VRML97 parser, lots of demos, etc) you can install that with::

    $ pip2.7 install "OpenGLContext-full==3.1.1"

Or you can clone it (including the tutorial sources) with::

    $ git clone https://github.com/mcfletch/openglcontext.git

or (for GitHub usage)::

    $ git clone https://github.com/mcfletch/pyopengl.git

The `documentation pages`_ are useful for looking up the parameters and semantics of
PyOpenGL calls.

.. _`tutorial page`: http://pyopengl.sourceforge.net/context/tutorials/index.html
.. _`documentation pages`: http://pyopengl.sourceforge.net/documentation/


Running Tests
--------------

You can run the PyOpenGL test suite from a source-code checkout, you will need:

* git (for the checkout)
* GLUT (FreeGLUT)
* GLExtrusion library (libgle)
* GLU (normally available on any OpenGL-capable machine)
* tox (`pip install tox`)

Running the test suite from a top-level checkout looks like::

    $ tox

The result being a lot of tests being run in a matrix of environments.
All of the environment will pull in pygame, some will also pull in
numpy. Some will have accelerate, and some will not.

.. image:: https://travis-ci.org/mcfletch/pyopengl.svg?branch=master
    :target: https://travis-ci.org/mcfletch/pyopengl
    :alt: Travis Tests

.. image:: https://ci.appveyor.com/api/projects/status/MikeCFletcher/pyopengl/branch/master
    :target: https://ci.appveyor.com/project/MikeCFletcher/pyopengl
    :alt: Appveyor Build

.. image:: https://img.shields.io/pypi/v/pyopengl.svg
    :target: https://pypi.python.org/pypi/pyopengl
    :alt: Latest PyPI Version

.. image:: https://img.shields.io/pypi/dm/pyopengl.svg
    :target: https://pypi.python.org/pypi/pyopengl
    :alt: Monthly download counter
=======
>>>>>>> 2a9e84a9... Update readme.rst

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=QtPyHammer-devs_PyOpenGL3&metric=bugs)](https://sonarcloud.io/dashboard?id=QtPyHammer-devs_PyOpenGL3)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=QtPyHammer-devs_PyOpenGL3&metric=ncloc)](https://sonarcloud.io/dashboard?id=QtPyHammer-devs_PyOpenGL3)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=QtPyHammer-devs_PyOpenGL3&metric=sqale_index)](https://sonarcloud.io/dashboard?id=QtPyHammer-devs_PyOpenGL3)
# Goals of this fork

To update the entire PyOpenGL binding to Python 3.8+

This will include use of f-strings, type hints & removing Python 2.7 support where readbility can be improved

To generate docstrings from either text files or https://www.khronos.org/registry/OpenGL-Refpages/gl4/html on install  

(This repo is huge so automating changes will be very important)

To inform the programmer of errors in a way that is instructive & state aware, while retaining C OpenGL error codes

Catch errors the OpenGL C implementation communicates poorly (non-square cubemap texture etc.)

To remove the need for numpy, with quick the translation of python types into bytes handled invisibly:

```c
void glBufferData(GLenum target, GLsizeiptr size, const void * data, GLenum usage);
```
```python
def gl.buffer.set_data(target: gl.buffer_type, data: List[bytes], usage: gl.buffer.usage, size=-1)
    """if size == -1, default to len(data)"""
```

Before being passed to C, translate iterable to bytestring, taking hints from other arguments  

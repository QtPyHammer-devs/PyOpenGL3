#! /usr/bin/env python
from distutils.command.install_data import install_data
import os
import sys
from setuptools import setup


extra_commands = {}

master_folder = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
with open(os.path.join(master_folder, "README.md"), "r") as readme:
    long_description = readme.read()

sys.path.insert(0, ".")
metadata = dict(
    version="3.1.5",
    license="BSD",  # which variant? no advertising clause
    author="Jared Ketterer",
    author_email="haveanotherbiscuit@gmail.com",
    url="https://github.com/QtPyHammer-devs/PyOpenGL3",  # no builds to release yet
    download_url="https://github.com/QtPyHammer-devs/PyOpenGL3",  # PyPI release? contact mcfletch first
    keywords="Graphics, 3D, OpenGL, GLU, GLUT, GLE, GLX, EXT, ARB, Mesa, ctypes",
    classifiers=["License :: OSI Approved :: BSD License",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3",
                 "Topic :: Multimedia :: Graphics :: 3D Rendering",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 "Intended Audience :: Developers"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)


def is_a_package(folder_path):
    return os.path.isfile(os.path.join(folder_path, "__init__.py"))


def packages_in(master_folder):
    """Find all packages under this directory"""
    out = list()
    for folder_path, directories, files in os.walk(master_folder):
        if is_a_package(folder_path):
            out.append(folder_path.replace("/", "."))
    return out


requirements = []
if sys.hexversion < 0x2050000:  # checking if python 3?
    requirements.append("ctypes")


class smart_install_data(install_data):
    def run(self):
        # need to change self.install_dir to the library dir
        install_cmd = self.get_finalized_command("install")
        self.install_dir = getattr(install_cmd, "install_lib")
        # should create the directory if it doesn"t exist!!!
        return install_data.run(self)


extra_commands["install_data"] = smart_install_data

if sys.platform == "win32":
    # binary versions of GLUT and GLE for Win32 (sigh)
    DLL_DIRECTORY = os.path.join("OpenGL", "DLLS")
    datafiles = [(DLL_DIRECTORY,
                  [os.path.join(DLL_DIRECTORY, file) for file in os.listdir(DLL_DIRECTORY) if
                   os.path.isfile(os.path.join(DLL_DIRECTORY, file))])]
else:
    datafiles = []


if __name__ == "__main__":
    setup(name="PyOpenGL3",
          packages=packages_in("OpenGL"),
          description="Standard OpenGL bindings for Python",
          options={"sdist": {"formats": ["gztar", "zip"],
                             "force_manifest": True}},
          data_files=datafiles,
          cmdclass=extra_commands,
          **metadata)

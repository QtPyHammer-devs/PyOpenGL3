#! /usr/bin/env python
"""Simple setup script that installs Tcl/Tk Togl widget into PyOpenGL"""
import sys
import os
import logging
import urllib
import tarfile
import zipfile
import fnmatch

import OpenGL

log = logging.getLogger("togl-setup")

if sys.maxint > 2**32:
    suffix = "-64"
else:
    suffix = ""
# These three define what software we"re going to install...
BASE_URL = "https://downloads.sourceforge.net/project/togl/Togl"
TOGL_VERSION = "2.0"
COMPILED_TK_VERSION = "8.4"


def get_url(filename):
    return f"{BASE_URL}/{TOGL_VERSION}/Togl{TOGL_VERSION}-{COMPILED_TK_VERSION}-{filename}?use_mirror=iweb"


urls = {"win32": get_url("Windows.zip"),
        "linux2": get_url("Linux.tar.gz"),
        "linux2-64": get_url("Linux64.tar.gz"),
        "darwin": get_url("MacOSX.tar.gz")}
# urls["linux2-64"] = "Togl2.0-8.4-Linux64.tar.gz"

WANTED_FILES = f"Togl{TOGL_VERSION}-{COMPILED_TK_VERSION}-*/lib/Togl{TOGL_VERSION}/*"


def setup(key=None, force=False):
    """Do setup by creating and populating the directories

    This incredibly dumb script is intended to let you unpack
    the Tcl/Tk library Togl from SourceForce into your
    PyOpenGL 3.0.1 (or above) distribution.

    Note: will not work with win64, both because there is no
        win64 package and because we don"t have a url defined
        for it."""
    if key is None:
        key = f"{sys.platform}{suffix}"
    log.info(f"Doing setup for platform key: {key}")
    target_directory = os.path.join(os.path.dirname(OpenGL.__file__), "Tk", f"togl-{key}")
    log.info(f"Target directory: {target_directory}")
    if key not in urls:
        log.error(f"URL for platform key {key} is not present, please update script")
        sys.exit(1)
    if os.path.exists(target_directory):
        return False

    url = urls[key]
    log.info(f"Downloading: {url}")
    filename, headers = urllib.urlretrieve(url)
    log.info("Downloaded to: {filename}")
    if not os.path.isdir(target_directory):
        log.warning(f"Creating directory: {target_directory}")
        try:
            os.makedirs(target_directory)
        except OSError:
            log.error(f"Unable to create directory: {target_directory}")
            sys.exit(2)

    # extract from .tar.gz
    if ".tar.gz" in url:
        log.info("Opening TarFile")
        fh = tarfile.open(filename, "r:gz")

        def getnames():
            return fh.getnames()

        def getfile(name):
            return fh.extractfile(name)

    # extract from .zip
    elif ".zip" in url:
        log.info("Opening ZipFile")
        fh = zipfile.ZipFile(filename)

        def getnames():
            return fh.namelist()

        def getfile(name):
            return fh.open(name)
    try:
        for name in getnames():
            log.debug(f"Found file: {name}")
            if fnmatch.fnmatch(name, WANTED_FILES):
                if not name.endswith("/"):
                    log.info(f"Found wanted file: {name}")
                    source = getfile(name)
                    try:
                        new = os.path.join(target_directory, os.path.basename(name))
                        log.info(f"Writing file: {new}")
                        open(new, "wb").write(source.read())
                    finally:
                        if hasattr(source, "close"):
                            source.close()
    finally:
        fh.close()
        if filename != url:
            os.remove(filename)
    return True


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if sys.argv[1:]:
        if sys.argv[1] == "all":
            keys = urls.keys()
        else:
            keys = sys.arv[1:]
        for key in keys:
            setup(key)
    else:
        setup()

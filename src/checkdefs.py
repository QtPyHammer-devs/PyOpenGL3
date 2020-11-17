#! /usr/bin/env python
import logging
import os
import subprocess

log = logging.getLogger("checker")


def main():
    env = running_env = os.environ.copy()
    for path, dirs, files in os.walk(os.path.join("..", "OpenGL", "raw")):
        for file in files:
            if file.endswith(".py"):
                log.debug(f"Check: {file}")
                if "osmesa" in path.split(os.sep):
                    running_env = env.copy()
                    running_env["PYOPENGL_PLATFORM"] = "osmesa"
                elif "EGL" in path.split(os.sep):
                    running_env = env.copy()
                    running_env["PYOPENGL_PLATFORM"] = "egl"
                elif "WGL" in path.split(os.sep):
                    log.debug("Skipping win32")
                    continue
                else:
                    running_env = env

                try:
                    subprocess.check_call(["python", os.path.join(path, file)],
                                          env=running_env)
                except subprocess.CalledProcessError:
                    log.error(f"Failure loading: {path}/{file}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()

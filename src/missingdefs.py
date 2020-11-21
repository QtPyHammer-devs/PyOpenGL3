#! /usr/bin/env python
"""Quick script to check for all entry points being defined"""
import json
import logging
import re


lmatch = re.compile(r"^\w+[ \t]*\([^)]+\)")
comment = re.compile(r"([ \t]*\#.*)|passthru\:")
param = re.compile(r"[ \t]+(?P<type>[^ \t]+)[ \t]+(?P<name>[^ \t]+)([ \t]+(?P<details>.*))?")
functions = {}
log = logging.getLogger("missing")


def module_for_category(category):
    """Return the OpenGL.GL.x module for the given category name"""
    if category.startswith("VERSION_"):
        name = "OpenGL.GL"
    else:
        owner, name = category.split("_", 1)
        if owner.startswith("3"):
            owner = owner[1:]
        name = "OpenGL.GL.{owner}.{name}"
    return __import__(name, {}, {}, name.split("."))


def main():
    current = None
    for line in open("gl.spec"):
        line = line.rstrip("\n").rstrip("\r")
        if lmatch.match(line):
            current = {"": line.strip(),
                       "name": line.strip().split("(")[0]}
            functions[current["name"]] = current
        elif not current:
            pass
        elif comment.match(line):
            pass
        else:
            match = param.match(line)
            if match:
                current.setdefault(match.group("type"), []).append((match.group("name"), match.group("details")))
    OUT_MAPPING = {}
    categories = {}
    for key, func in functions.items():
        assert "category" in func, func
        categories.setdefault(func["category"][0][0], []).append(func)
        out_params = dict([x for x in func.get("param", []) if "out" in x[1].split()])
        if out_params:
            OUT_MAPPING["gl" + key] = out_params
    with open("gl_out_parameters.json", "w") as file:
        file.write(json.dumps(OUT_MAPPING, indent=2, sort_keys=True))
    for category, funcs in sorted(categories.items()):
        try:
            module = module_for_category(category)
        except ImportError:
            log.error(f"Whole category missing: {category}")
        else:
            log.info(f"Checking category: {category}")
            for func in funcs:
                funcname = func["name"]
                if not hasattr(module, funcname):
                    log.error(f"Missing entry point {funcname} in module {module.__name__}")


if __name__ == "__main__":
    logging.basicConfig()
    main()

# -*- coding: utf-8 -*-

name = "ocio"

version = "2.0.0"

authors = [
    "Sony Pictures"
]

requires = [
    "gcc",
    "cmake",
    "python",
    "glew",
]

def commands():
    env.OCIO_ROOT = "{root}"
    env.OCIO_LOCATION = "{root}"
    env.OPENCOLORIO_ROOT = "{root}"
    env.OPENCOLORIO_LOCATION = "{root}"
    env.PATH.append("{root}/bin")

uuid = "repository.ocio"

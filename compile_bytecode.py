#!/usr/bin/env python
#Script to compile python scripts into python bytecode.
#Written by Quinn Neufeld
#Jan. 7th 2019
import py_compile
from sys import argv

if len(argv) < 2:
    print("Usage: compile_bytecode <file...>")
    exit()
elif argv[1] == "-h" or argv[1] == "--help":
    print("Usage: compile_bytecode <file...>")
    exit()

files = argv[1:]
for path in files:
    py_compile.compile(path)

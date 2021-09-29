#!/usr/bin/env python3
"""
rename-jpg-large.py
Renames .jpg_large files to .jpg files
written by Quinn Neufeld
Nov. 10th 2019
Sept. 29 2021 - Removed progutil dependency
"""

import os
from sys import argv

HELP_MSG = """Usage: rename-jpg-large.py <file(s)/dir(s)>
Recursively renames files / dirs from .jpg_large files to .jpg files."""

def rename_path(path: str):
    """Recursively renames files in a directory / renames an individual file
    path -- the path to the file / directory to rename"""
    #Rename files if path is a dir
    if os.path.isdir(path):
        for subpath in os.listdir(path):
            rename_path(path + "/" + subpath)
        return
    
    #Rename file
    os.rename(path, path.replace(".jpg_large", ".jpg"))

#Verify inputs
if len(argv) < 2 or "-h" in argv or "--help" in argv:
    exit(1)

#Rename each path given to us
for arg in argv[1:]:
    rename_path(arg)
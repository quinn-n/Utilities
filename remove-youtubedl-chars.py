#!/usr/bin/env python3

# Removes the extra chars on a file created by youtube-dl.
# Ex. test-ioedjfack.webm -> test.webm
# Written / Maintained by Quinn Neufeld
# June 25th 2019
# Sept. 29 2021 - Removed progutil dependency

from sys import argv
import os

HELP_MSG = "Usage: remove-youtubedl-chars <file(s)>"

def get_paths(path: str):
    """Returns the files and paths of everything in a dir"""
    paths = os.listdir(path)
    files = []
    dirs = []
    for p in paths:
        if os.path.isdir(p):
            dirs.append(p)
        else:
            files.append(p)
    return files, dirs

def str_contains(string: str, search: str):
    """Returns true if search is in string"""
    return string.count(search) > 0

def is_youtubedl(path: str):
    """Returns true if the file at path is a youtube-dl file
    Basically checks for a '-', some chars and a '.'"""
    #Check that a - and a . are in the path
    if not (str_contains(path, "-") and str_contains(path, ".")):
        return False
    #Make sure the pattern is -, <chars>, .
    if path.rindex(".") < path.rindex("-") + 1:
        return True
    else:
        return False
    
def get_ending(path: str):
    """Returns the ending of the file at path"""
    last_pos = path.rindex(".")
    return path[last_pos:]

def get_name(path: str):
    """Returns the file name (without the ending)"""
    last_pos = path.rindex(".")
    return path[:last_pos]
    
def rename_file(path: str):
    """Renames a youtube-dl file"""
    ending = get_ending(path)
    name = get_name(path)
    last_dash = name.rindex("-")
    outpath = name[:last_dash] + ending
    print("Renaming " + path + " to " + outpath)
    os.rename(path, outpath)

def rename_dir(path: str):
    """Renames a directory with youtube-dl files"""
    files, dirs = get_paths(path)
    for fi in files:
        rename_file(fi)
    del files
    for d in dirs:
        rename_dir(d)

def rename_path(path: str):
    """Renames a path wheter it is a directory or a file"""
    if os.path.isdir(path):
        rename_dir(path)
    else:
        rename_file(path)

if len(argv) < 2 or "-h" in argv or "--help" in argv:
    print(HELP_MSG)
    exit(1)

for fi in argv[1:]:
    rename_path(fi)
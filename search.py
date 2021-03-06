#!/usr/bin/env python3
"""
search.py <file/dir> <str>
Recursively searches file contents for a given string.
Outputs the files that contain the string.
Written by Quinn Neufeld. <Quinn Neufeld@gmail.com>
March 23rd 2019
"""
from time import sleep
import os
from sys import argv
import progutil

HELP_MSG = "Usage: search.py <path> <string> [-v]\nSearches a file / directory for a given string.\n-v = verbose mode"
VERBOSE = False

def verbose_print(str):
    """Prints str only if verbose mode is enabled."""
    if VERBOSE:
        print(str)

def search_file(path, search):
    """Returns true if the file at path contains a given string."""
    #Make sure the script doesn't crash on a read error for a single file.
    try:
        fi = open(path, "r")
        fi_str = fi.read()
        fi.close()
    except:
        verbose_print("Could not open " + path)
        return False

    if fi_str.count(search) > 0:
        return True
    else:
        return False

def search_path(path, search):
    """Searches a directory/file for a given string."""
    #If it's a directory, run search_path on the contents.
    if os.path.isdir(path):
        files = os.listdir(path)
        for fi in files:
            fipath = path + "/" + fi
            search_path(fipath, search)
    #If it's a file, search the file.
    else:
        if search_file(path, search):
            print(path)

def main():
    """Program's main function."""
    if not progutil.check_inputs(argv, 3, HELP_MSG):
        return False
    #Set verbose
    args = progutil.parse_inputs(argv, guaranteed=["v"])
    global VERBOSE
    VERBOSE = args["v"]
    del args
    #Search path.
    search_path(argv[1], argv[2])

main()

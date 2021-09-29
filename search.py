#!/usr/bin/env python3
"""
search.py <file/dir> <str>
Recursively searches file contents for a given string.
Outputs the files that contain the string.
Written by Quinn Neufeld. <Quinn Neufeld@gmail.com>
March 23rd 2019
Sept. 29 2021 - Removed progutil dependency
Sept. 29 2021 - Added support for multiple search terms and fuzzy support
"""
from time import sleep
import os
from sys import argv

HELP_MSG = """Usage: search.py <path> <string[s]> [-h] [-v]
-h / --help - prints this message and exits
-v / --verbose - verbose mode
-f / --fuzzy - fuzzy search, passes check if one string matches instead of all strings"""
VERBOSE = False
EXCLUDED_SEARCH_TERMS = ("-v", "--verbose", "-h", "--help", "-f", "--fuzzy")

def verbose_print(s: str):
    """Prints str only if verbose mode is enabled."""
    if VERBOSE:
        print(s)

def search_file(path: str, search: list[str], fuzzy: bool) -> bool:
    """Returns true if the file at path contains every string in search."""
    #Make sure the script doesn't crash on a read error for a single file.
    try:
        fi = open(path, "r")
        fi_str = fi.read()
        fi.close()
    except:
        verbose_print("Could not open " + path)
        return False

    if not fuzzy:
        for s in search:
            if not s in fi_str:
                return False
        return True
    else:
        for s in search:
            if s in fi_str:
                return True
        return False

def search_path(path: str, search: list[str], fuzzy: bool):
    """Searches a directory/file for a given string."""
    #If it's a directory, run search_path on the contents.
    if os.path.isdir(path):
        files = os.listdir(path)
        for fi in files:
            fipath = path + "/" + fi
            search_path(fipath, search, fuzzy)
    #If it's a file, search the file.
    else:
        if search_file(path, search, fuzzy):
            print(path)

def main():
    """Program's main function."""
    if len(argv) < 3 or "-h" in argv or "--help" in argv:
        print(HELP_MSG)
        return False
    #Set verbose
    global VERBOSE
    if "-v" in argv or "--verbose" in argv:
        VERBOSE = True
    else:
        VERBOSE = False
    if "-f" in argv or "--fuzzy" in argv:
        fuzzy = True
    else:
        fuzzy = False
    search_terms = []
    for a in argv[2:]:
        if not a in EXCLUDED_SEARCH_TERMS:
            search_terms.append(a)
    #Search path.
    search_path(argv[1], search_terms, fuzzy)

if __name__ == "__main__":
    main()

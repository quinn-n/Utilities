#!/usr/bin/env python3
"""Replaces text in files. Now recursively.
Usage: replace.py <file> <to replace> <to replace with> <[times to replace]>
Written by Quinn Neufeld.
Sept. 29 2021 - Removed progutil dependency"""

from sys import argv
import os

HELP_MSG = "Usage: replace.py <file/dir> <to replace> <to replace with> <[times to replace]>"

def main():
    """main function"""
    #check inputs.
    if len(argv) < 4 or "-h" in argv or "--help" in argv:
        print(HELP_MSG)
        exit(1)

    path = argv[1]
    to_rep = argv[2]
    to_rep_with = argv[3]
    times = 0
    if len(argv) > 4:
        times = int(argv[4])

    if os.path.isfile(path):
        replace_file(path, to_rep, to_rep_with, times=times)
    else:
        replace_dir(path, to_rep, to_rep_with, times=times)

def replace_dir(path, to_rep, to_rep_with, times=0):
    """Recursively replaces every instance of to_rep with to_rep_with in path."""
    for fipath in os.listdir(path):
        fullpath = path + "/" + fipath
        if os.path.isfile(fullpath):
            replace_file(fullpath, to_rep, to_rep_with, times=times)
        else:
            replace_dir(fullpath, to_rep, to_rep_with, times=times)


def replace_file(path, to_rep, to_rep_with, times=0):
    """Replaces to_rep with to_rep_with in the file at path."""
    fi = open(path, "r")
    try:
        lines = fi.readlines()
    except:
        print("Had an error while opening file " + path)
        fi.close()
        return
    fi.close()
    new_lines = []
    for line in lines:
        if times == 0:
            line = line.replace(to_rep, to_rep_with)
        else:
            line = line.replace(to_rep, to_rep_with, times)
        new_lines.append(line)
    outfi = open(path, "w")
    outfi.writelines(new_lines)
    outfi.close()

main()

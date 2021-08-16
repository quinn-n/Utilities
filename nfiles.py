#!/usr/bin/env python3

"""
nfiles.py <[dir]>
Prints out the number of files either in a provided directory or in a local directory
written by Quinn Neufeld
September 8th 2020
"""

import os
from sys import argv

def print_help():
    """Prints help message"""
    print("Usage: nviles.py [-h] <[dir]>")
    print("Prints out the number of files in a directory, or in the local directory if no directory is provided.")
    print("-h -- help, prints this message")

if "-h" in argv or "--help" in argv:
    print_help()
    exit(1)

path = "."
if len(argv) > 1:
    path = argv[1]

print(len(os.listdir(path)))

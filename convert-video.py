#!/usr/bin/env python3

"""
convert-video.py
Converts video files to audio files
Written by Quinn Neufeld
June 24th 2019
March 25th 2021 Replaced string concats with os.path.join where applicable
Sept. 29 2021 - Removed progutil dependency
"""

import os
from sys import argv
import multiprocessing as mp

HELP_MSG = """Usage: convert-video.py <indir> [-o outdir]
Converts video files in a directory and puts them into an output dir.
-o <outdir> - Specify what directory to write output files to. Defaults to out/
Requires ffmpeg."""

DEFAULT_OUTDIR = "out/"

#Verify inputs
if len(argv) < 2 or "-h" in argv or "--help" in argv:
    print(HELP_MSG)
    exit(1)

indir = argv[1]

#Set output dir to either the default or the one given by the command line
outdir = DEFAULT_OUTDIR
i = 1
while i < len(argv):
    if "-o" in argv[i]:
        outdir = argv[i + 1]
        i += 1
    i += 1

def ensure_exists(path: str):
    """If a directory does not exist, creates it"""
    if not os.path.exists(path):
        os.mkdir(path)

def remove_ending(path: str):
    """Removes the file ending"""
    last_loc = path.rfind(".")
    return path[:last_loc]

def convert_file(name: str):
    """Converts a file in the input dir to a file in the output dir"""
    inpath = os.path.join(indir, name)
    no_end = remove_ending(name)
    outpath = os.path.join(outdir, no_end + ".mp3")
    print("Converting file " + inpath + " to " + outpath)
    os.system("ffmpeg -i " + escape_string(inpath) + " " + escape_string(outpath))

def escape_string(s: str):
    """Inserts escape characters in s"""
    outstr = ""
    for c in s:
        outstr += "\\" + c
    return outstr

files = os.listdir(indir)

#Make sure the output directory exists
ensure_exists(outdir)

for name in files:
    convert_file(name)

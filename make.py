#!/usr/bin/env python
import os
from sys import argv

ignored_files = ["make.py", "makefile", ".git", "README.txt"]
#renamed_files = {"repeat.py":"repeat", "replace.py":"replace", "type.py":"type"}

def last_idx(string, search):
    """Returns the last index of search in string."""
    for i in range(len(string) - 1, -1, -1):
        if string[i] == search:
            return i
    return -1

def remove_extension(fi):
    """Removes file extension"""
    last_pos = last_idx(fi, ".")
    return fi[:last_pos]

def localinstall():
    homepath = os.popen("echo ~").read()[0:-1]
    if not os.path.exists(homepath + "/.local/"):
        os.mkdir(homepath + "/.local/")
    if not os.path.exists(homepath + "/.local/bin/"):
        os.mkdir(homepath + "/.local/bin/")
    workingdir = os.popen("pwd").read()[0:-1]
    files = os.listdir(".")
    for fi in files:
        if not fi in ignored_files:
            print("linking " + fi + " to " + fi[:-3])
            os.system("ln -sf " + workingdir + "/" + fi + " " + homepath + "/.local/bin/" + fi[:-3])

def install():
    """Installs scripts to /usr/bin/"""
    #Requires root
    files = os.listdir(".")
    #Go over each file. If it's in ignored_files, ignore it. Else, copy it to /usr/bin/
    for fi in files:
        if not fi in ignored_files:
            #Strip fi of file extension (.py)
            new_fi = remove_extension(fi)
            os.system("cp " + fi + " /usr/bin/" + new_fi)


function = ""
if len(argv) >= 2:
    function = argv[1] + "()"
exec(function)

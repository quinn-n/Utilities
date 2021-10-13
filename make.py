#!/usr/bin/env python3
import os
from shutil import copyfile

import click


ignored_files = ["make.py", "makefile", ".git", "README.txt", "requirements.txt"]
#renamed_files = {"repeat.py":"repeat", "replace.py":"replace", "type.py":"type"}

@click.group()
def make() -> None:
    pass

@make.command()
def localinstall() -> None:
    """Installs scripts to $HOME/.local/bin/
    """
    homepath = os.environ["HOME"]
    if not os.path.exists(os.path.join(homepath, ".local")):
        os.mkdir(os.path.join(homepath, ".local"))
    if not os.path.exists(os.path.join(homepath, ".local", "bin")):
        os.mkdir(os.path.join(homepath, ".local", "bin"))

    workingdir = os.environ["PWD"]
    files = os.listdir(".")
    for fi in files:
        if not fi in ignored_files:
            #Strip fi of file extension (.py)
            stripped_fi = "".join(fi.split(".")[:-1])
            print("linking " + fi + " to " + stripped_fi)
            os.symlink(os.path.join(workingdir, fi), os.path.join(homepath, ".local", "bin", stripped_fi))

@make.command()
def install() -> None:
    """Installs scripts to /usr/bin/ (requires sudo)"""
    #Requires root
    files = os.listdir(".")
    #Go over each file. If it's in ignored_files, ignore it. Else, copy it to /usr/bin/
    for fi in files:
        if not fi in ignored_files:
            #Strip fi of file extension (.py)
            stripped_fi = "".join(fi.split(".")[:-1])
            copyfile(fi, os.path.join("/usr", "bin", stripped_fi))


if __name__ == "__main__":
    make()

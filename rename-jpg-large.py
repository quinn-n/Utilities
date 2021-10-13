#!/usr/bin/env python3
"""
rename-jpg-large.py
Renames .jpg_large files to .jpg files
written by Quinn Neufeld
Nov. 10th 2019
Sept. 29 2021 - Removed progutil dependency
Oct. 11 2021 - Moved CLI over to click
"""

import os

import click


HELP_MSG = """Usage: rename-jpg-large.py <file(s)/dir(s)>
Recursively renames files / dirs from .jpg_large files to .jpg files."""

@click.command()
@click.argument("path", type=str, required=True)
def rename_path(path: str) -> None:
    """Recursively renames files in a directory / renames an individual file
    """
    #Rename files if path is a dir
    if os.path.isdir(path):
        for subpath in os.listdir(path):
            rename_path(os.path.join(path, subpath))
        return
    
    #Rename file
    os.rename(path, path.replace(".jpg_large", ".jpg"))

if __name__ == "__main__":
    rename_path(None)

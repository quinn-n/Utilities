#!/usr/bin/env python3
"""Replaces text in files. Now recursively.
Usage: replace.py <file> <to replace> <to replace with> <[times to replace]>
Written by Quinn Neufeld.
Sept. 29 2021 - Removed progutil dependency"""

from sys import argv
import os

import click


@click.command()
@click.argument("path", required=True, type=click.Path(exists=True))
@click.argument("to_replace", required=True, type=str)
@click.argument("to_replace_with", required=True, type=str)
@click.argument("times", default=0, type=int)
def replace(*args, **kwargs):
    """Replaces instances of to_replace with to_replace_with in path
    """
    path = kwargs["path"]
    to_replace = kwargs["to_replace"]
    to_replace_with = kwargs["to_replace_with"]
    times = kwargs["times"]
    if os.path.isfile(path):
        replace_file(path, to_replace, to_replace_with, times=times)
    else:
        replace_dir(path, to_replace, to_replace_with, times=times)


def replace_dir(path: str, to_rep: str, to_rep_with: str, times: int = 0):
    """Recursively replaces every instance of to_rep with to_rep_with in path

    Args:
        path (str): Directory to replace strings in
        to_rep (str): String literal to be replaced
        to_rep_with (str): String literal to replace to_rep with
        times (int, optional): Maximum nuber of times to replace in each file. Defaults to 0.
    """
    for fipath in os.listdir(path):
        fullpath = os.path.join(path, fipath)
        if os.path.isfile(fullpath):
            replace_file(fullpath, to_rep, to_rep_with, times=times)
        else:
            replace_dir(fullpath, to_rep, to_rep_with, times=times)


def replace_file(path: str, to_rep: str, to_rep_with: str, times: int = 0):
    """Replaces to_rep with to_rep_with in the file at path

    Args:
        path (str): File path to replace strings in
        to_rep (str): String literal to be replaced
        to_rep_with (str): String literal to do the replacing
        times (int, optional): Maximum number of times to replace. Defaults to 0.
    """
    fi = open(path, "r")
    try:
        lines = fi.readlines()
    except:
        click.echo(f"Had an error while opening file: {path}")
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


if __name__ == "__main__":
    replace()

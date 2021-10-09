#!/usr/bin/env python3
"""
search.py <file/dir> <str>
Recursively searches file contents for a given string.
Outputs the files that contain the string.
Written by Quinn Neufeld. <Quinn Neufeld@gmail.com>
March 23rd 2019
Sept. 29 2021 - Removed progutil dependency
Sept. 29 2021 - Added support for multiple search terms and fuzzy support
Oct. 8 2021 - Added support for regular expressions and moved arguments and options to click
"""
from time import sleep
import os
from sys import argv
import re

import click

VERBOSE = 0


def verbose_print(s: str, msg_verbosity: int) -> None:
    """Prints str only if verbose mode is enabled."""
    if VERBOSE >= msg_verbosity:
        click.echo(s)


def search_file(path: str, search: list[str], fuzzy: bool, regex: bool) -> bool:
    """Returns true if the file at path contains every string in search."""
    # Make sure the script doesn't crash on a read error for a single file.
    try:
        fi = open(path, "r")
        fi_str = fi.read()
        fi.close()
    except:
        verbose_print("Could not open " + path, 1)
        return False

    if not fuzzy:
        for s in search:
            if not regex:
                if not s in fi_str:
                    return False
            else:
                if re.search(s, fi_str) is None:
                    return False
        return True
    else:
        for s in search:
            if not regex:
                if s in fi_str:
                    return True
            else:
                if re.search(s, fi_str) is not None:
                    return True
        return False


def search_path(path: str, search: list[str], fuzzy: bool, regex: bool) -> None:
    """Searches a directory/file for a given string."""
    # If it's a directory, run search_path on the contents.
    if os.path.isdir(path):
        files = os.listdir(path)
        for fi in files:
            fipath = os.path.join(path, fi)
            search_path(fipath, search, fuzzy, regex)
    # If it's a file, search the file.
    else:
        if search_file(path, search, fuzzy, regex):
            if VERBOSE < 2:
                click.echo(path)
            verbose_print(f"match: {path}", 2)
        else:
            verbose_print(f"no match: {path}", 2)


@click.command()
@click.argument("filename", required=True, type=str)
@click.option("-v", "--verbose", count=True, type=int, default=0, help="verbose mode. More v = more verbose")
@click.option("-f", "--fuzzy", is_flag=True, type=bool, default=False, help="fuzzy search, passes check if one string matches instead of all strings")
@click.option("-r", "--re", "--regex", is_flag=True, default=False, type=bool, help="regex mode, matches regular expressions rather than string literals")
@click.argument("search_terms", required=True, type=str, nargs=-1)
def search(*args, **kwargs: [bool, int]) -> None:
    """Program's main function."""
    # Set verbose
    global VERBOSE
    VERBOSE = kwargs["verbose"]
    verbose_print(f"Got verbose level: {VERBOSE}", 1)
    # Search path.
    search_path(kwargs["filename"], kwargs["search_terms"],
                kwargs["fuzzy"], kwargs["re"])


if __name__ == "__main__":
    search()

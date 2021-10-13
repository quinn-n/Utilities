#!/usr/bin/env python3
# Echos the number of instances of a given list of searches in a file / directory
# Written by Quinn Neufeld
# Oct. 12 2021 - Complete rewrite, now supports recursion & uses click for CLI.
# Also added support for regular expressions and recursion

import os
import re

import click


def search_dir(path: str, search: list[str], regex: bool) -> dict[int]:
    """Searches a path and returns the number of instances of each item in search

    Args:
        path (str): path to search
        search (list[str]): list of strings or regular expressions to search for
        regex (bool): If true, matches regular expressions instead of string literals

    Returns:
        dict[int]: Dict with the number of occurances of each item in search
    """
    out = {}
    for p in os.listdir(path):
        subpath = os.path.join(path, p)
        if os.path.isdir(subpath):
            res = search_dir(subpath, search, regex)
            for k in res:
                if not k in out:
                    out[k] = res[k]
                else:
                    out[k] += res[k]
        else:
            res = search_file(subpath, search, regex)
            for k in res:
                if not k in out:
                    out[k] = res[k]
                else:
                    out[k] += res[k]
    return out

def search_file(path: str, search: list[str], regex: bool) -> dict[int]:
    """Searches a file and returns the number of instances of each item in search

    Args:
        path (str): File path to search
        search (list[str]): List of strings / regular expressions to search for
        regex (bool): If true, matches regular expressions instead of string literals

    Returns:
        dict[int]: Dict with the number of occurances of each item in search
    """
    try:
        with open(path, "r") as fi:
            fi_str = fi.read()
    except UnicodeDecodeError:
        return {}

    out = {}
    if not regex:
        for s in search:
            out[s] = fi_str.count(s)
    else:
        for s in search:
            out[s] = len(re.finditer(s, fi_str))
    return out

@click.command()
@click.argument("path", type=str, required=True)
@click.argument("search", type=str, nargs=-1, required=True)
@click.option("-r", "--regex", is_flag=True, default=False, type=bool, help="regex mode, matches regular expressions rather than string literals")
def get_instances(path: str, search: tuple[str], regex: bool) -> None:
    """Echos the number of instances of each search string in path
    """
    res = search_dir(path, search, regex)
    for k in res:
        click.echo(f"{k}: {res[k]}")

if __name__ == "__main__":
    get_instances(None, None, None)

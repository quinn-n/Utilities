#!/usr/bin/env python3
# Echos the length of each provided argument
# If no arguments are provided, echos the length of stdin
# Written by Quinn Neufeld
# Oct. 12 2021 - Complete rewrite, now supports multiple arguments and reading from stdin
# Also moved CLI to click

import os
from sys import stdin

import click


def stdin_len() -> int:
    """Returns the length of stdin

    Returns:
        int: The number of bytes read from stdin
    """
    return len(stdin.read())

@click.command()
@click.argument("strings", nargs=-1, type=str, required=False)
@click.option("-f", "--file", multiple=True, type=str, required=False, help="File to print the length of")
def length(strings: list[str], file: list[str]) -> None:
    """Echos the length of each provided string
    If no strings are provided, echos the length of stdin
    """
    if file:
        for f in file:
            click.echo(f"{f}: {os.path.getsize(f)} bytes")
    if strings:
        for s in strings:
            click.echo(f"{s}: {len(s)}")
    if not file and not strings:
        click.echo(f"stdin: {stdin_len()} bytes")

if __name__ == "__main__":
    length(None, None)

#!/usr/bin/env python3
# Copies a file / directory from src to dest.
# Prints the completion status
# Written by Quinn Neufeld
# Oct. 11 2021 - Rewrote to support recursion and moved CLI to click

import os
import multiprocessing as mp
from time import sleep
from shutil import copyfile

import click


def copy(src: tuple[str], dest: str) -> None:
    """Copies a path from src to dest.

    Args:
        src (list[str]): Source path
        dest (str): Dest path
    """
    for s in src:
        if os.path.isdir(s):
            if not os.path.exists(os.path.join(s)):
                os.mkdir(os.path.join(dest, s))
            for f in os.listdir(s):
                copy((os.path.join(s, f),), os.path.join(dest, s, f))
        else:
            if os.path.isdir(dest):
                copyfile(s, os.path.join(dest, s))
            else:
                copyfile(s, dest)

@click.command()
@click.argument("src", type=str, required=True, nargs=-1)
@click.argument("dest", type=str, required=True)
def copy_status(src: list[str], dest: str) -> None:
    """Copies files from src to dest. Prints the status as a percent.
    """
    copy_process = mp.Process(target=copy, args=(src, dest,))
    copy_process.start()

    src_size = sum(os.path.getsize(s) for s in src)
    while not os.path.exists(dest):
        sleep(.0001)
    while copy_process.is_alive():
        dest_size = os.path.getsize(dest)
        click.echo(f"{round(dest_size / src_size * 100, 2)}% complete\r", nl=False)
        sleep(.02)
    
    copy_process.join()
    click.echo("100% complete")

if __name__ == "__main__":
    copy_status(None, None)

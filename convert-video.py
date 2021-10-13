#!/usr/bin/env python3

"""
convert-video.py
Converts video files to audio files
Written by Quinn Neufeld
June 24th 2019
March 25th 2021 Replaced string concats with os.path.join where applicable
Sept. 29 2021 - Removed progutil dependency
Oct. 11 2021 - Moved CLI to click
"""

import os
import multiprocessing as mp

import click


def ensure_exists(path: str) -> None:
    """Ensures a direcotry / file exists.
    If nothing exists at path, creates a directory

    Args:
        path (str): Path to ensure exists
    """
    if not os.path.exists(path):
        os.mkdir(path)

def remove_ending(path: str) -> str:
    """Removes file ending

    Args:
        path (str): Path to remove ending from

    Returns:
        str: New path without ending
    """
    last_loc = path.rfind(".")
    return path[:last_loc]

def convert_file(srcfi: str, destfi: str) -> None:
    """Runs srcfi through ffmpeg and writes the result to destfi

    Args:
        srcfi (str): Video file to convert
        destfi (str): Audio file to write to
    """
    click.echo(f"Converting {srcfi} to {destfi}")
    os.system(f"ffmpeg -i {escape_string(srcfi)} {escape_string(destfi)}")

def escape_string(s: str) -> str:
    """Escapes out every character in s

    Args:
        s (str): String to escape

    Returns:
        str: Escaped string
    """
    outstr = ""
    for c in s:
        outstr += "\\" + c
    return outstr

def convert_dir(srcdir: str, outdir: str) -> None:
    """Converts video files in a directory to audio files

    Args:
        srcdir (str): source directory
        outdir (str): destination directory
    """
    ensure_exists(srcdir)
    ensure_exists(outdir)
    for file in os.listdir(srcdir):
        convert_file(os.path.join(srcdir, file), os.path.join(outdir, remove_ending(file) + ".mp3"))


@click.command()
@click.argument("srcdir", required=True, type=str)
@click.option("-o", "--outdir", required=False, type=str, default="out/", help="Specify what directory to output files to. Defaults to out/")
def convert_videos(src: str, outdir: str) -> None:
    """Converts video(s) at src to audio files and writes them to outdir
    """
    if os.path.isdir(src):
        convert_dir(src, outdir)
    else:
        convert_file(src, os.path.join(outdir, remove_ending(src) + ".mp3"))

if __name__ == "__main__":
    convert_videos(None, None)

#!/usr/bin/env python3

from PIL import Image
import sys

import click


@click.command()
@click.argument("src", required=True, type=str)
@click.argument("dest", required=True, type=str)
def convert_image(src: str, dest: str) -> None:
    """Converts an image from one type to another using Pillow
    """
    image = Image.open(src)
    image.save(dest)

if __name__ == "__main__":
    convert_image(None, None)

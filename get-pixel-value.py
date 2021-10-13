#!/usr/bin/env python3
# Echos the rgb & greyscale values of the pixel currently under the mouse cursor
# Written by Quinn Neufeld
# Oct. 12 2021 - Rewrote greyscale function to actually be right & moved CLI over to click
from time import sleep

import click
import pyautogui


def greyscale(rgb: tuple[int]) -> int:
    """Returns weighted greyscale value from rgb

    Args:
        rgb (tuple[int]): (r, g, b) - tuple of rgb values from 0 - 255

    Returns:
        int: greyscale value calculated from rgb tuple
    """
    return rgb[0] * .299 + rgb[1] * .587 + rgb[2] * .114

@click.command()
@click.argument("delay", required=False, default=0, type=int)
def get_pixel_value(delay: int) -> None:
    """Echos the rgb & greyscale values of the pixel currently under the mouse cursor
    """
    sleep(delay)
    x, y = pyautogui.position()
    im = pyautogui.screenshot(region=(x, y, 1, 1))
    pixels = im.load()
    colour_vals = pixels[0, 0]
    click.echo(f"Got {colour_vals} at {(x, y)} with a greyscale of {greyscale(colour_vals)}")

if __name__ == "__main__":
    get_pixel_value(None)

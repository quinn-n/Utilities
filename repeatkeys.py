#!/usr/bin/env python
# Types a string a given number of times.
# requires pyautogui.
# Written by Quinn Neufeld
# Feb. 15th 2019
# Sept. 29 2021 - Removed progutil dependency
# Oct. 8 2021 - Rewrote to use click

from sys import argv
from time import sleep

import click
import pyautogui


@click.command()
@click.argument("string", required=True, type=str)
@click.argument("times", required=True, type=int)
@click.argument("delay", type=int, default=1)
def repeatkeys(*args, **kwargs):
    """Repeatedly types string a given number of times. If no delay is given, defaults to 1.
    """
    string = kwargs["string"]
    times = kwargs["times"]
    delay = kwargs["delay"]
    sleep(delay)
    for _ in range(times):
        pyautogui.typewrite(string)


if __name__ == "__main__":
    repeatkeys()

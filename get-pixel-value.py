#!/usr/bin/env python3
from time import sleep
from sys import argv
import pyautogui

HELP_MSG = """Usage: get-pixel-value <delay>
Sleeps for delay seconds and gets the colour values of the pixel your cursor is on."""

def avg(nums):
    """Returns the average for all the numbers in nums."""
    total = sum(nums)
    return total / len(nums)

def main():
    """Program's main function"""
    if len(argv) < 2:
        print(HELP_MSG)
        exit(1)
    elif argv[1] == "-h" or argv[1] == "--help":
        print(HELP_MSG)
        exit()
    sleep_time = int(argv[1])
    sleep(sleep_time)
    x, y = pyautogui.position()
    im = pyautogui.screenshot(region=(x, y, 1, 1))
    pixels = im.load()
    colour_vals = pixels[0, 0]
    print("Got " + str(colour_vals) + " at " + str((x, y)) + " with a greyscale of " + str(avg(colour_vals)))

main()

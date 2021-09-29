#!/usr/bin/env python
# Types a string a given number of times.
# requires pyautogui.
# Written by Quinn Neufeld
# Feb. 15th 2019
# Sept. 29 2021 - Removed progutil dependency
from sys import argv
from time import sleep
import pyautogui
HELP_MSG = """Usage: repeatkeys <string> <times> <[delay]>
Types out string a given number of times after delay. (If no delay is given, defaults to 1 second.)"""

def main():
    """Program's main function."""
    if len(argv) < 3 or "-h" in argv or "--help" in argv:
        print(HELP_MSG)
        exit(1)
    string = argv[1]
    times = int(argv[2])
    #Check if we're given a delay or not. If not, select default (1 sec)
    if len(argv) >= 4:
        delay = float(argv[3])
    else:
        delay = 1
    sleep(delay)
    del delay
    for _ in range(times):
        pyautogui.typewrite(string)

main()

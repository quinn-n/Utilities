#!/usr/bin/env python
import pyautogui
from time import sleep
from sys import argv
time_to_wait = 1.
if len(argv) < 2:
    print("Usage: type <string> <[delay]>")
    print("Types string after delay seconds. If no delay is given, uses 1 second.")
    exit()
elif argv[1] == "-h" or argv[1] == "--help":
    print("Usage: type <string> <[delay]>")
    print("Types string after delay seconds. If no delay is given, uses 1 second.")
    exit()

string = argv[1]
if len(argv) > 2:
    time_to_wait = float(argv[2])

sleep(time_to_wait)
pyautogui.typewrite(string)

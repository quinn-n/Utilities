#!/usr/bin/env python3
from sys import argv
from os import system
if len(argv) < 2:
    print("Usage: "+argv[0]+" <program>")
    print("Redirects stdout to /dev/null.")
    exit()

command = argv[1]
system(command+" >> /dev/null &")

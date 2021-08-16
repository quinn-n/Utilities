#!/usr/bin/env python3
import sys
import random
import time
import os

if len(sys.argv) < 3:
    print("Usage: "+sys.argv[0]+" <music files>")
    print("Uses mpg123, so it will only accept mp3 files.")
    sys.exit()
music = sys.argv[1:]

choice = None
while True:
    oldChoice = choice
    choice = random.choice(music)
    if choice != oldChoice:
        os.system("mpg123 -v '"+choice+"'")
        time.sleep(.25)

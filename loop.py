#!/usr/bin/env python3
import sys
import os
import time
if len(sys.argv) < 2:
    print("Usage: loop <songs>")
    print("Uses mpg123 to play songs. (so it obviously requires you to install mpg123)")
    sys.exit()
songs = sys.argv[1:]
songString = ""
for song in songs:
    songString = songString+"'"+song+"' "
#print("Will run mpg123 "+songString)
while True:
    os.system("mpg123 -v "+songString)
    time.sleep(.5)

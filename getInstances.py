#!/usr/bin/env python3
import sys
if len(sys.argv) < 3:
    print("Usage: "+sys.argv[0]+" <file> <searches>")
    print("Finds the number of instances of each search in file")
    sys.exit()
searches = sys.argv[2:]
file = open(sys.argv[1],"r")
text = file.read()
file.close()
for search in searches:
    lastInstance = 0
    locations = []
    while lastInstance != -1:
        lastInstance = text.find(search,lastInstance+1)
        locations.append(lastInstance)
    print("Found "+str(len(locations))+" instances of "+search)

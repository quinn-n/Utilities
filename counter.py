#!/usr/bin/env python3
import sys
if len(sys.argv) < 2:
    print("Usage: "+sys.argv[0]+" <delay>")
    print("Gets the number of times per second a delay will happen- ex. .05 will return 20.")
    sys.exit()
timer = float(sys.argv[1])
i = 0
counter = 0
while i <= 1:
    i = i+timer
    counter = counter+1
print(str(counter))

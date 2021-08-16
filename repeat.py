#!/usr/bin/env python3
import sys
if len(sys.argv) < 3:
    print("Usage: "+sys.argv[0]+" <string> <number>")
    print("Repeat string number times")
    sys.exit()

for _ in range(int(sys.argv[2])):
    print(sys.argv[1],end="")
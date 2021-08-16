#!/usr/bin/env python3
import sys
if len(sys.argv) < 2: #make sure we got a string.
    print("Usage: length <string>")
    print("Prints the length of a string.")
    sys.exit()
print(str(len(sys.argv[1])))

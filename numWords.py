#!/usr/bin/env python3
import sys
if len(sys.argv) < 2:
    print("Usage: "+sys.argv[0]+" <words>")
    sys.exit()
words = sys.argv[1]
numSpaces = words.count(" ")
numNewlines = words.count("\n")
numWords = numSpaces+numNewlines+1
print(str(numWords))

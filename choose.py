#!/usr/bin/env python3
import sys
import random
import math
if len(sys.argv) < 3:
    print("Usage: "+sys.argv[0]+" <options>")
    print("Randomly picks an option.")
    sys.exit()
selection = math.floor(random.uniform(1,len(sys.argv)))
print(sys.argv[selection])

#!/usr/bin/env python3
from PIL import Image
import sys
if len(sys.argv) < 3:
    print("Usage: "+sys.argv[0]+" <input file> <output file>")
    sys.exit()
image = Image.open(sys.argv[1])
image.save(sys.argv[2])

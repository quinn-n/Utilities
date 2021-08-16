#!/usr/bin/env python3
from PIL import Image
import sys
if len(sys.argv) < 2:
    print("Usage: "+sys.argv[0]+" <file>")
    sys.exit()
imagePath = sys.argv[1]
image = Image.open(imagePath).convert("L")
pixels = image.load()
width = image.size[0]
height = image.size[1]
finishedImage = []
for y in range(height):
    cachePixels = []
    for x in range(width):
        cachePixels.append(round(pixels[x,y]/255))
    finishedImage.append(cachePixels)
for row in finishedImage:
    print(row)

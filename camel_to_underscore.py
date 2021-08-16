#!/usr/bin/env python3
#Written by Quinn Neufeld$
#
#Turns camelCase variable names into underscore_spacing names.
from sys import argv
if len(argv) < 2:
    print("Usage: " + argv[0] + " <file>")
    exit(1)

CAPITALS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

path = argv[1]

infile = open(path, "r")

lines = []
cache = infile.readline()
while cache != "":
    lines.append(cache[:-1])
    cache = infile.readline()

infile.close()

new_lines = []
#split the file into lines, then words
for line in lines:
    words = line.split(" ")
    new_words = []
    for word in words:
        new_word = ""
        for char in word:
            #if the current char is a capital, append an underscore and the lowercase version of the char. Else, append the char.
            if not char in CAPITALS:
                new_word += char
            else:
                new_word += "_" + char.lower()
        new_words.append(new_word)
    #turn all the words into a single string again.
    word_str = ""
    for word in new_words:
        word_str += word + " "
    new_lines.append(word_str)

"""
print("New file:")
for line in new_lines:
    print(line)
"""
outfile = open(path, "w")
for line in new_lines:
    outfile.write(line + "\n")

outfile.close()

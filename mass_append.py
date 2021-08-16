#!/usr/bin/env python3
import sys
import multiprocessing
import math
if len(sys.argv) < 4:
    print("Usage: mass-append <filePath> <number of times to append> <string to append>")
    print("Use with caution.")
    sys.exit()
filePath = sys.argv[1]
timesToAppend = int(sys.argv[2])
stringToAppend = sys.argv[3]
file = open(filePath,"a")
cores = multiprocessing.cpu_count()
print("Detected "+str(cores)+" cores")
def append(file,data,times):
    for loopNum in range(times):
        file.write(stringToAppend)
    file.close()
processes = []
if timesToAppend > cores:
    timesPerCore = math.floor(timesToAppend/cores)
    for i in range(cores):
        processes.append(multiprocessing.Process(target=append,args=(file,stringToAppend,timesPerCore)))
    for i in range(len(processes)):
        processes[i].start()

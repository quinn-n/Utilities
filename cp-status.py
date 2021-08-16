#!/usr/bin/env python3
import sys
import os
import multiprocessing as mp
from time import sleep
SLEEP_TIME = .1

def copy(source, destination):
    os.system("cp "+source+" "+destination)

if len(sys.argv) < 3:
    print("Usage: "+sys.argv[0]+" <source> <destination>")
    print("Copies files from one location to the other. Prints the status as a percent.")
    sys.exit()

source = sys.argv[1]
destination = sys.argv[2]

copyProcess = mp.Process(target=copy,args=(source,destination,))
copyProcess.start()

sourceSize = os.path.getsize(source)
while not os.path.exists(destination):
    sleep(.01)
destinationSize = os.path.getsize(destination)

while sourceSize != destinationSize:
    sourceSize = os.path.getsize(source)
    destinationSize = os.path.getsize(destination)
    #overwrite old percent prints with spaces so we don't end up with a '100% complete.3% complete.'
    print("                                                                          ",end="\r",flush=True)
    print(str((destinationSize / sourceSize) * 100) + "% complete.", end="\r", flush=True)
    sleep(SLEEP_TIME)
print("\ndone copying files")

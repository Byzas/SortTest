#python 3
import time
from quicksort import quicksort
from fusionsort import fusionsort

import sys

#To do big amount of recursive
sys.setrecursionlimit(10000)


#Get the integer list from IntList.txt file
#Basically, it contains 10.000 integers between 1 and 1.000.000.000
with open('IntList.txt', 'r') as f:
    IntList = [int(x) for x in f.read().split(' ')]
    print(IntList)

#Launch the different sort

#quicksort
startTime = time.time()
quicksort(IntList, 0, len(IntList)-1)
print("Quicksort done in %s seconds" % (time.time()-startTime))
print(IntList)

#fusionsort
startTime = time.time()
fusionsort(IntList)
print("Fusion done in %s seconds" % (time.time()-startTime))
print(IntList)
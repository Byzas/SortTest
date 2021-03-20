#python 3
import time
from quicksort import quicksort
from fusionsort import fusionsort
from heapsort import heapsort

import sys

#To do big amount of recursive
sys.setrecursionlimit(10000)


def getIntlist():
    #Get the integer list from IntList.txt file
    #Basically, it contains 10.000 integers between 1 and 1.000.000.000
    with open('IntList.txt', 'r') as f:
        IntList = [int(x) for x in f.read().split(' ')]
        return IntList

#Launch the different sort

IntList = getIntlist()
print(IntList)
#quicksort
startTime = time.time()
quicksort(IntList, 0, len(IntList)-1)
print("Quicksort done in %s seconds" % (time.time()-startTime))
print(IntList)

IntList = getIntlist()
print(IntList)
#fusionsort
startTime = time.time()
IntList = fusionsort(IntList)
print("Fusionsort done in %s seconds" % (time.time()-startTime))
print(IntList)

#IntList = getIntlist()
#print(IntList)
#heapsort
#startTime = time.time()
#heapsort(IntList)
#print("Heapsort done in %s seconds" % (time.time()-startTime))
#print(IntList)
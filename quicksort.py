#python 3

def partition(Intlist, first, last):
    small_ele = (first-1)
    #decided arbitrarily
    pivot = Intlist[last]

    for i in range(first, last):

        #Enter if the current element is inferior or equal to the pivot
        if Intlist[i] <= pivot:
            small_ele = small_ele+1
            #soap the small element with the current
            Intlist[small_ele], Intlist[i] = Intlist[i], Intlist[small_ele]

    #soap the small element with the last used as pivot
    Intlist[small_ele+1], Intlist[last] = Intlist[last],Intlist[small_ele+1]
    return small_ele+1


# Recursive quicksort
def quicksort(IntList, first, last):
    if len(IntList) == 1:
        return IntList
    if first < last:
        partitioned = partition(IntList, first, last)

        # recursively launch the quick sort for two partitioned part of the list
        quicksort(IntList, first, partitioned-1)
        quicksort(IntList, partitioned+1, last)
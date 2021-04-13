# python 3

#recursive fusion algorithm
def fusion(ListA, ListB):
    #Deal with an empty list.
    if not ListA:
        return ListB
    if not ListB:
        return ListA
    print(ListA)
    print("-----")
    print(ListB)
    #compare the first element of each list and do fusion in recursive
    if ListA[0] <= ListB[0]:
        buffList = []
        buffList.append(ListA[0])
        return buffList + fusion(ListA[1:len(ListA)], ListB)
    else:
        buffList = []
        buffList.append(ListB[0])
        return buffList + fusion(ListA, ListB[1:len(ListB)])


def fusionsort(Intlist):
    #Check if List size is one so it's already sorted
    if len(Intlist) == 1:
        return Intlist
    else:
        # Divide the list in two part and send in the fusion algorithm
        return fusion(Intlist[0:int(len(Intlist) / 2)], Intlist[int(len(Intlist) / 2) :len(Intlist)])

#python 3



class BinaryTree(object):

    def __init__(self):
        self.fathervalue = 0
        self.father = None
        self.currentvalue = 0
        self.childLeftValue = 0
        self.childLeft = None
        self.childRightValue = 0
        self.childRight = None

    def setChildLeft(self, value, child):
        self.childLeft = child
        self.childLeftValue = value

    def setChildRight(self, value, child):
        self.childRight = child
        self.childRightValue = value

    def setCurrent(self, value):
        self.currentvalue = value

    def setFather(self,value, father):
        self.father = father
        self.fathervalue = value

def getHighFreeBranch(tree):

    if tree.childLeft is None:
        return tree.childLeft
    elif tree.childRight is None:
        return tree.childRight
    elif tree.childLeft.childLeft is None:
        return tree.childLeft.childLeft
    elif tree.childLeft.childRight is None:
        return tree.childLeft.childRight
    elif tree.childRight.childLeft is None:
        return tree.childRight.childLeft
    elif tree.childRight.childRight is None:
        return tree.childRight.childRight
    else:
        return getHighFreeBranch(tree.childLeft)

def soapFatherAscending(currentbranch):

    if currentbranch.father is not None:
        if currentbranch.fathervalue > currentbranch.currentvalue:
            currentbranch.value, currentbranch.fathervalue = currentbranch.fathervalue, currentbranch.currentvalue, currentbranch
            soapFatherAscending(currentbranch.father)
    else:
        return

def getLowerBranch(tree):

    if tree.childLeft is None and tree.childRight is None:
        return tree
    if tree.childRight is None:
        return getLowerBranch(tree.childLeft)
    else:
        return getLowerBranch(tree.childRight)

def updateTree(tree):

    if tree.currentvalue < tree.childLeftValue:
        tree.currentvalue, tree.childLeftValue, tree.childLeft.currentvalue = tree.childLeftValue, tree.currentvalue, tree.currentvalue
        updateTree(tree.childLeft)
    elif tree.currentvalue < tree.childRightValue:
        tree.currentvalue, tree.childRightValue, tree.childRight.currentvalue = tree.childRightValue, tree.currentvalue, tree.currentvalue
        updateTree(tree.childRight)


def heapsort(Intlist):

    tree = BinaryTree()

    if len(Intlist) == 1:
        return Intlist

    #Init root
    tree.setCurrent(Intlist[0])
    previousBranch = tree
    print(Intlist)
    for i in range(1, len(Intlist)-1):

        # Init new branch
        currentBranch = BinaryTree()
        currentBranch.setCurrent(Intlist[i])
        currentBranch.setFather(previousBranch.currentvalue, previousBranch)

        #update father informations
        if previousBranch.childLeft is None:
            previousBranch.setChildLeft(currentBranch.currentvalue, currentBranch)
        else:
            previousBranch.setChildRight(currentBranch.currentvalue, currentBranch)

        #compare current value with father
        if currentBranch.currentvalue > currentBranch.fathervalue and currentBranch.father is not None:
            currentBranch.currentvalue, currentBranch.fathervalue, previousBranch.currentvalue = previousBranch.currentvalue, currentBranch.currentvalue, currentBranch.currentvalue
            soapFatherAscending(currentBranch.father)


        previousBranch = getHighFreeBranch(tree)

    nw_list= []

    for i in range(0, len(Intlist)-1):

        nw_list = [tree.currentvalue] + nw_list
        #Put the lowest value in the tree in the top
        currentBranch = getLowerBranch(tree)
        tree.currentvalue = currentBranch.currentvalue
        updateTree(tree)
        del currentBranch

    return nw_list

#!/bin/env python3
def addlist(alist):
    for i in range(0, len(alist)):
        for j in range(i+1, len(alist)):
            print(alist[i], "+", alist[j], "=", alist[i] + alist[j])

def snap(alist):
    for i in range(0, len(alist)-1):
        if alist[i] == alist[i+1]:
            print("YES")
            return
    print("NO")

def bingo(alist):
    for i in range(0, len(alist)-1):
        for j in range(i+1, len(alist)):
            if alist[i] == alist[j]:
                return 1
    return 0

def evenadd(alist):
    listsum = 0
    for i in range(0, len(alist)):
        if (alist[i] % 2) == 0:
            listsum = listsum + alist[i]
    return listsum

def evenoddsort(alist):
    blist = []
    blist = []
    for i in range(0, len(alist)):
        if (alist[i] % 2) == 0:
            blist.append(alist[i])
        else:
            blist.append(alist[i])
    print("B", blist, "C", blist)

def evenoddsmallest(alist):
    # set to disallow 0 in list
    blist = 0
    clist = 0
    for i in range(0, len(alist)):
        # check for even
        if (alist[i] % 2) == 0:
            # even
            if alist[i] < blist or blist == 0:
                # a lower even
                blist = alist[i]
        else:
            # odd
            if alist[i] < clist or clist == 0:
                # a lower odd
                clist = alist[i]
    print("B", blist, "C", clist)


def locations(alist):
    # pass me a list
    mykeys = set()
    mykeys.update(alist)
    mydict = {}
    for i in range(0, len(alist)):
        # jrw
        mydict
    return mydict


list1 = [1, 3, 4, 8, 2]
list2 = [1, 3, 4, 3]
list3 = [1, 3, 4, 5, 8]
lista = [1, 3, 3, 6, 4, 8, 1]
#addlist(list1)
#snap(list2)
# if bingo(list2):
#     print("YES")
# else:
#     print("NO")

# print(evenadd (list1))
# print(sum(list1)-evenadd (list1))

#evenoddsort(list1)
#evenoddsmallest(list3)
#myset = set (list3)
# set1 = set()
# set1.update(list3)
locations(lista)

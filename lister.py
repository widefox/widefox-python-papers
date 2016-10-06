#!/bin/env python3
def addlist(alist):
    for i in range(0, len(alist)-1):
        for j in range(i+1, len(alist)):
            print('{}+{}={}'.format(alist[i], alist[j], alist[i] + alist[j]))

def snap(alist):
    for i in range(0, len(alist)-1-1):
        if alist[i] == alist[i+1]:
            print("YES")
            return
    print("NO")

def bingo(alist):
    for i in range(0, len(alist)-1-1):
        for j in range(i+1, len(alist)):
            if alist[i] == alist[j]:
                return 1
    return 0

def evenadd(alist):
    listsum = 0
    for i in range(0, len(alist)-1):
        if (alist[i] % 2) == 0:
            listsum = listsum + alist[i]
    return listsum

def evenoddsort(alist):
    elist = []
    olist = []
    for i in range(0, len(alist)-1):
        if (alist[i] % 2) == 0:
            elist.append(alist[i])
        else:
            olist.append(alist[i])
    print("B={} C={}".format(elist, olist))

def evenoddsmallest(alist):
    # set to disallow 0 in list
    elist = 0
    olist = 0
    for i in range(0, len(alist)-1):
        # check for even
        if (alist[i] % 2) == 0:
            # even
            if alist[i] < elist or elist == 0:
                # a lower even
                elist = alist[i]
        else:
            # odd
            if alist[i] < olist or olist == 0:
                # a lower odd
                olist = alist[i]
    print("B={} C={}".format(elist, olist))

def locations(alist):
    # pass me a list
    mykeys = set()
    mykeys.update(alist)
    mydict = {}
    for i in range(0, len(alist)):
        # jrw - todo
        print(mydict)
    return mydict


list1 = [1, 3, 4, 8, 2]
list2 = [1, 3, 4, 3]
list3 = [1, 3, 4, 5, 8]
lista = [1, 3, 3, 6, 4, 8, 1]
addlist(list1)
snap(list2)
if bingo(list2):
    print("YES")
else:
    print("NO")

print(evenadd(list1))
print(sum(list1)-evenadd(list1))

evenoddsort(list1)
evenoddsmallest(list3)
myset = set(list3)
set1 = set()
set1.update(list3)
#todo
#locations(lista)

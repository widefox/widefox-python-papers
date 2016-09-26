#!/bin/env python2
def addlist(alist):
    for i in range(0, len(alist)):
        for j in range(i+1, len(alist)):
            print alist[i] , "+",  alist[j] , "=" , alist[i] + alist[j]

def snap(alist):
    for i in range(0, len(alist)-1):
        if (alist[i] == alist[i+1]):
            print "YES"
            return
    print "NO"

def bingo(alist):
    match=0
    for i in range(0, len(alist)-1):
        for j in range(i+1, len(alist)):
            if (alist[i] == alist[j]):
                return 1
    return 0

def evenadd(alist):
    sum = 0
    for i in range(0, len(alist)):
        if ((alist[i] % 2) == 0):
           sum = sum + alist[i]
    return sum

def evenoddsort(alist):
    B=[]
    C=[]
    for i in range(0, len(alist)):
        if ((alist[i] % 2) == 0):
           B.append (alist[i])
        else:
           C.append (alist[i])
    print "B", B , "C", C
           
def evenoddsmallest(alist):
    # set to disallow 0 in list
    B=0
    C=0
    for i in range(0, len(alist)):
        # check for even
        if ((alist[i] % 2) == 0):
            # even
            if (alist[i] < B or B == 0):
                # a lower even
                B = alist[i]
        else:
            # odd
            if (alist[i] < C or C == 0):
                # a lower odd
                C = alist[i]
    print "B", B , "C", C


def locations(a):
    # pass me a list
    mykeys=set()
    mykeys.update(a)
    mydict={}
    for i in range(0, len(a)):
        mydict
    return mydict


    
list1 = [1, 3, 4, 8, 2]
list2 = [1, 3, 4, 3]
list3 = [1, 3, 4, 5, 8]
a=[1,3,3,6,4,8,1]

# questions
addlist(list1)
#snap(list2)
# if bingo(list2):
#     print "YES"
# else:
#     print "NO"

# print evenadd (list1)
# print (sum(list1)-evenadd (list1))
    
#evenoddsort(list1)
#evenoddsmallest(list3)
#myset=set (list3)
# set1 = set()
# set1.update(list3)
locations(a)

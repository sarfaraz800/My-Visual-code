def Insertionsort(l):
    for sliceEnd in range(len(l)):
        pos=sliceEnd
        while pos > 0 and l[pos]<l[pos-1]:
            (l[pos],l[pos-1])=(l[pos-1],l[pos])
            pos=pos-1
    return (l)        

l=list(range(500,-1,-2))
print("Sorted list is ",Insertionsort(l))
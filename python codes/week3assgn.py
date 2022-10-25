#Program to count Hills and Valleys

def counthv(l):
    (h,v)=(0,0)
    for i in range(1,len(l)-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            h=h+1
        if l[i]<l[i-1] and l[i]<l[i+1]: 
            v=v+1
    l=[h,v]
    return (l)

def contracting(l):
    list1=[]
    for i in range(0,len(l)-1):
        list1.append(abs(l[i]-l[i+1])) #abs() return positive of negative
    #if list1!=list1.sort(reverse=True):
        #return (False)
    #else:
        #return (True)  
    for i in range(0,len(list1)-1):
        if list1[i]<=list1[i+1]:
            return (False)
    return (True)            

l = [-32,-11,10,-9,8,-7,6,-5,4,-3,2,-1]
print(contracting(l))
'''def leftrotate(m):
    for i in range(0,len(m)):
        for j in range (0,len(m)):
            
    return (m)'''        

#l= counthv([1,1,1,1,1,1,1,1])
#print("Number of Hills is ",l[0],"Number of valleys are ",l[1])
#m=[[1,2,3], [4,5,6], [7,8,9]]
#print(leftrotate(m))
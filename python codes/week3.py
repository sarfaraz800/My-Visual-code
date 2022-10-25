'''print(range(0,10)==[0,1,2,3,4,5,6,7,8,9])
l=list(range(0,10))
print(l)
n=100
print(type(n))
s=str(n)
print(s)
print(type(s))
integer=int(s)
print(integer)
print(type(integer))
integer=int("32x")
print(integer)
print(type(integer))

def apply(f,x,n):
    res=x
    for i in range(n):
        res=f(res)
    return (res)

def square(x):
    return(x*x)

def iseven(x):
    return(x%2==0)
l=list(map(square,filter(iseven,range(100))))    
print(l)
#f=apply
#print(f(square,5,2))
def findpos(l,v):
    i=0
    for x in l:
        if x==v:
            return (i)
        i=i+1
    return (-1)        
l=list(range(0,10+1))
print("ys")
print(findpos(l,3))
#l1=list(range(1,20+1,3))
l[3:]=l1
l[2]=50
l.reverse()
l.sort()
print(l)
print(l.index(1))

a=int("5",10)
print(a)'''

def mystery(l):
    print(l)
    if l == []:
        return(l)
    else:
        return(mystery(l[1:])+l[:1])

l=[22,14,19,65,82,55]
print(mystery(l))    


def intreverse(n):
    num=n%10
    n=n//10
    while n%10!=0:
        num=(num*10)+n%10
        n=n//10
    return (num)

def matched(s):
    opencount=0
    closecount=0
    for i in range(0,len(s)):
        if s[i] == "(":
            opencount=opencount+1
        elif s[i] == ")":
            closecount=closecount+1
    if opencount==closecount:
        return (True)
    else:
        return (False)                

def sumprimes(l):
    sum=0
    for i in range(0,len(l)):
        if prime(l[i]):
            sum+=l[i]
    return (sum)
def prime(n):
    return(factors(n)==[1,n])
def factors(n):
    lfact=[]
    for i in range(1,n+1):
        if n%i==0:
            lfact=lfact+[i]
    return(lfact)        

#print("Enter a number")
n=int(input("Enter a number\n"))    
print("Intreverse is ",intreverse(n))
#print("Enter a string")
s=str(input("Enter a string\n"))
print("Matched ?",matched(s))
#print("Enter the list value")
l=list(range(1,100+1,2))
print(l)
print("Sum of prime is ",sumprimes(l))
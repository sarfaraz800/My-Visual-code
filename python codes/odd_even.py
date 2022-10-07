def divides(m,n):
    if n%m==0:
        return (True)
    else:
        return (False)

def odd(n):
    return(not divides(2,n))

def even(n):
    return (divides(2,n))

print("Enter a number")
n=int(input())
print(n,"is odd? ",odd(n))
print(n,"is even? ",even(n))
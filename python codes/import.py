from math import sqrt
# from math import*   (also correct)
def sqroot(n):
    return (sqrt(n))
print("Enter a number")
n=int(input())
m=sqroot(n)
print("Square root is ",m)    
print(type(m))# print data type of m 
print(type(n))# print data type of n
def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return (n)
    else:
        return (gcd(n,m%n))          

m=int(input("Enter two number\n"))
n=int(input())
print("GCD is ",gcd(m,n))                
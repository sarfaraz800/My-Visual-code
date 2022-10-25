def fibonacci(n):
    if n==1 or n==2:
        return (1)
    else:
        return (fibonacci(n-1)+fibonacci(n-2))    

n=int(input("Enter a number\n"))
print("Fibonacci of ",n," is",fibonacci(n))        
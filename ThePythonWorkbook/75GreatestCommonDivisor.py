n=int(input("Enter first number?"))
m=int(input("Enter second number?"))

if n<m:
    d=n
    while n%d !=0 or m%d!=0:
        d-=1
    print("The greatest common divisor is:",d)
elif m<n:
    d=m
    while n%d!=0 or m%d!=0:
        d-=1
    print("The greatest common divisor is:",d)
else:
    print("The greatest common divisor is:",n)

    

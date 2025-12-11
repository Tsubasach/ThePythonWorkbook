n=int(input("Enter first number?"))
m=int(input("Enter second number?"))
j=0
if n<m:
    d=n
    while d>0:
        if n%d==0 and m%d==0:
            j+=d
        d-=1

    print("The greatest common divisor is:",j)
elif m<=n:
    d=m
    while d>0:
        if m%d==0 and n%d==0:
            j+=d
        d-=1
    print("The greatest common divisor is:",j)


    

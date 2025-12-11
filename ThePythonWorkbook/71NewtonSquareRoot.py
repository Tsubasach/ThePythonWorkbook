import math
square=int(input("Input Numer:"))
guess=square/2

enough=math.pow(guess,2) - square
while abs(enough) >= math.pow(10,-12):
    guess=0.5*(guess+(square/guess))
    enough=guess*guess - square
print(guess)


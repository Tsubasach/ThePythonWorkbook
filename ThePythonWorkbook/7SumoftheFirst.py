number=input("Enter Number: ")
if int(number) > 0:
    sum = int((int(number) * (int(number) +1 )) / 2)
    print("sum is:", sum)
else:
    print("put valid number")
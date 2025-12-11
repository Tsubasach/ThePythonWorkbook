lessthanone= input("HOw many bottles 1 or less than 1 liter? ")
while not lessthanone.isdigit():
    lessthanone= input("HOw many bottles 1 or less than 1 liter? ")

morethanone= input("HOw many bottles more than 1 liter?")
while not morethanone.isnumeric():
    morethanone= input("HOw many bottles more than 1 liter?")

if int(morethanone) > 0:
    mablagh1=int(morethanone) * 0.25
    print("your refund for less than one liter is: ",mablagh1,"$")
if int(lessthanone) > 0:
    mablagh2=int(lessthanone) * 0.10
    print("your refund for morethan one liter is: ",mablagh2,"$")
else:
    print("you dont put any bottle")

print("sum is:", morethanone + lessthanone)
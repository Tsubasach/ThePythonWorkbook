meal=input("How much is the meal costs? ")
while not meal.isdigit():
    print("How much is the meal costs? ")
if int(meal)>0:
    tax=int(meal) * 0.01
    tip=f"{int(meal) * 0.18:.2f}"
    print("tax is:", tax)
    #print(f"{tip:2f}")
    print("tip is:", tip)
    sum=f"{(float(meal) + float(tip) + float(tax)):.2f}"
print("the sum is: ", sum , "$" )

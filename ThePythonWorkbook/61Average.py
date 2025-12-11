user=int(input("Enter First number if you want to end press '0': "))
list=[]
while True:
    
    if user!=0:
        list.append(user)
        user=int(input("Enter numbers if you want to end press '0': "))
    elif user==0 and len(list)>=2:
        average=sum(list)/len(list)
        print("The Average is:",average)
        break
    else:
        print("Wrong")
        user=int(input("Enter numbers "))
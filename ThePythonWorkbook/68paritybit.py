user=input("Enter 8 bit ")
count=0
if len(user)<=8:
    for i in user:
        if i=="1":
            count+=1


    if count % 2==0:
        print("Parity bit is 0")
    else:
        print("Parity bit is 1")
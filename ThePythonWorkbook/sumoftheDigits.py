number=input("Enter Four Digits")
while True:
   
    if len(number) == 4:
        
        sum=int(number[0])+int(number[1])+int(number[2])+int(number[3])
        print(number[0],"+",number[1],"+",number[2],"+",number[3],"=",int(sum))
        break
    else:
        number=input("Enter Exactly Four Digits")
        




'''print("Welcome to OUR Zoo")
guest2=int(input("Enter the Guests Below 2 years Old? [press 0 to Skip] "))
guest3=int(input("Enter the Guests Between 3 to 12 years Old? [press 0 to Skip]"))
guest4=int(input("Enter the Guests Between 12 to 65 years Old? [press 0 to Skip]"))
guest5=int(input("Enter the Guests more than 65 years Old? [press 0 to Skip]"))

if guest2 !=0:
    print("continueing...") 
else:
    print("continueing...")  
        
if guest3 != 0:
        guest3t=(guest3) * 14
else:
    print("continueing...")  
if  guest4 != 0:
    guest4t=guest4 * 23
else:
    print("continueing...")  
if  guest5 != 0:
        guest5t=guest5 * 18
else:
    print("continueing...")  

total=guest3t+guest4+guest5t
print(total)
'''

        
total=0.0
while True:
    guest=input("Enter the Guests Ages: (Press Enter to quit)")
    if guest != " ":   
         
        if 0 < int(guest) <= 2:
            continue
        elif 3 <= int(guest) <=12:
            total+=14
            
        elif 12<int(guest)<65:
            total+=23
           
        elif int(guest)>=65:
            total+=18
               
    else:
        break

print("Total Admission is: {%.2f}" % round(total,2))

        
    


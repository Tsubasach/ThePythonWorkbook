user=input("Choose From letter Grades \n [A+ , A , A- , B+] \n ")

dicti={"A+":"4.0","A":"4.0","A-":"3.7","B+":"3.3"}
while True:
 user=user.replace(" ","")
 if user.isalpha and len(user)<=2:
    
    if user[0].islower():
        user0=user[0].replace(user[0],user[0].upper())
        user=user0+user[1]

    if user in dicti:
            print("Your Grade equivalent is:",dicti[user])
            break
    else:
            print("Wrong!Try again...")
            user=input("Choose From letter Grades \n [A+ , A , A- , B+] \n ")
 
 else:
    print("WRONG INPUT")
    user=input("Choose From letter Grades \n [A+ , A , A- , B+] \n ")

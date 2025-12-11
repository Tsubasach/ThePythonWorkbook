user=input("Enter Chess position?")
white=["a","c","e","g"]
white1=["b","d","f","h"]
#row=["1","2","3","4","5","6","7","8"]


while True:
    if len(user) == 2 and int(user[1].isdigit()):
        if 1 <= int(user[1]) <= 8:
            if int(user[1]) % 2 == 0 and user[0] in white:
                print("Its White")
                break
            elif not int(user[1]) % 2 == 0 and user[0] in white:
                print("its black")
                break
            elif int(user[1]) % 2 == 0 and user[0] in white1:
                print("Its Black")
                break
            elif not int(user[1]) % 2 == 0 and user[0] in white1 :
                print("its White")
                break
            else:
                print("wrong")
            user=input("Enter Chess position (1)?")
        else:
            print("wrong")
            user=input("Enter Chess position(2)?")
    else:
        print("wrong Again")
        user=input("Enter Chess position(3)?")

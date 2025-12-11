user=input("Input rating")

while True:
    if int(user) % 2 == 0 :
        if float(user)==0.0:
            print("It Unacceptable performance")
            print("You dont get any raises")
            break
        if float(user)==0.4:
                inc=0.4*2400
                print("It acceptable performance")
                print("You get",inc)
                break
        if float(user)>=0.6:
            meri=float(user)*2400
            print("It Meritorious performance")
            print("You get",meri)
            break
        else:
            print("Wrong")
            break
    else:
        print("Wrong(1)")
        user=input("Input rating(1)")
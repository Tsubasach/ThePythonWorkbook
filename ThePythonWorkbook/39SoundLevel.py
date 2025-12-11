user=input("Enter decibels Number?:")
while True:
    if not user.isalpha() and not user=="":
        if  float(user) < 40:
            print("Its quiter than Quiet Room Decibels")
            break
        if float(user)==40:
            print("Its Quiet Room Decibels")
            break
        if 40<float(user)<70:
            print("Its between Quiet Room and Alarm clock Decibels")
            break
        if float(user)==70:
            print("Its Alarm Clock Decibels")
            break
        if 70<float(user)<106:
            print("Its Between Alarm clock and Gas lawnmower Decibels")
            break
        if float(user)==106:
            print("Its Gas lawnmower Decibels")
            break
        if 106<float(user)<130:
            print("Its Between Gas lawnmower and Jackhammer Decibels")
            break
        if float(user)==130:
            print("Its Jackhammer Decibels")
            break
        if float(user) > 130:
            print("Its louder than JackHammer Decibels")
            break
    else:
        user=input("Enter Number bigger than 0?:")


num=input("Input positive Number?: ")
while True:
   
    if num.isnumeric():
        
            if int(num) % 2==0 and int(num) > 0:

                print("Its EVEN")
                break
            else:
                print("Its ODD")
                break
    else:
        num=input("PLEASE INPUT POSITIVE NUMBER?: ")
          
import msvcrt



print("Press keys to get Holiday : \n 1 ==> January 1 \n 2 ==> July 1 \n 3 ==> December 25 ")


  # returns something like b'y' or b'n'
while True:
    getLetter = msvcrt.getch() 

    if getLetter == b'1':
        print("New year’sday")
        break
    if getLetter == b'2':
        print("Canada day")
        break
    if getLetter == b'3':        
        print(" Christmas day")
        break
    else:
        print("OOPS! Wrong number!Try again! \n  1 ==> January 1 \n 2 ==> July 1 \n 3 ==> December 25 ")
        getLetter = msvcrt.getch()
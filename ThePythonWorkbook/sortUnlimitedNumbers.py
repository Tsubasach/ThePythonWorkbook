list1=[]
#num=input("Enter First number or press 'e' to End: ")
#لیست را از کاربر میگیریم
#while True:
num = " "
i=1
while True:
    num= input(f"Enter number {i} or press e to END :")
    if num != "e" :
            found_digit = True
            for char in num:
                if not char.isdigit() and not "-":
                    found_digit = False
                    break
                # stop checking once a digit is found
                if found_digit:
                    list1.append(num)
                    i=i+1
                    break
                
            else:
                 print(f"Please enter number {i} again or press e to END :")
    else:
        print("the list is:",list1)
        break



def sortlist(list2):
    n=1
    for n in range(len(list2)-1): 
        j=0
        a=0
        for j in range(len(list2)-1):
            if int(list2[j]) > int(list2[j+1]):
                a=list2[j]
                list2[j]=list2[j+1]
                list2[j+1]=a
    print(list2)
             


    
sortlist(list1)

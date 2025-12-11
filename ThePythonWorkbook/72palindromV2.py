message=input("Enter your String? ")
j=""

for i in message:
    j=i+j

if j==message:
        print("its palindromic")
else:
        print("Its not")


##VERS2
'''
message=input("Enter your String? ")


j=message[::-1]

if j==message:
        print("its palindromic")
else:
        print("Its not")'''

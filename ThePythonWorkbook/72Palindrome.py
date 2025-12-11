message=input("Enter your String? ")

j=""
for i in message:
    if i.isalpha() and i != " " :
        j=j+i 

    
    
print(j)       
print(j[::-1])
k=j[::-1]
if j.lower()==k.lower():
        print("its palindromic")
else:
        print("Its not")


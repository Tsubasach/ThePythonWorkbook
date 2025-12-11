user=input("Put number of Sides?")

while True:
    if user.isnumeric():    
        if 3<=int(user)<=10:

            shape={3:"Triangle",4:"Square",5:"Pentagon",6:"Hexagon",7:"Heptagon",8:"Octagon",9:"nonagon",10:"Decagon"}
            print(shape[int(user)]) 
            break
        else:
            user=input("Input numbers between 3 to 10")
            

    else:
        user=input("Input positive number:")
    
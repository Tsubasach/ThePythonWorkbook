message=input("what is your message?")
shift=int(input("How many shifts?"))
#list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
j=""
coded=""
NumericError=False
#if message.isalpha():
if shift >=1 : # Encode Section
    for i in message:#range(len(message)):
        if 48 <=ord(i)<=57:
            NumericError=True
        #print(i,ord(i))
        if 65 <= ord(i) <= 90 :
            if ord(i)+shift > 90:
                j=j+chr(ord(i)+shift-26)#i.replace(i,chr(ord(i)+shift)-28)        
            else: 
                j=j+chr(ord(i)+shift)#i.replace(i,chr(ord(i)+shift))
            #coded+=j
        
        elif 97 <= ord(i) <= 122 :
            if ord(i)+shift > 122:
                j=j+chr(ord(i)+shift-26)#i.replace(i,chr(ord(i)+shift)-28)        
            else: 
                j=j+chr(ord(i)+shift)#i.replace(i,chr(ord(i)+shift))  
        elif ord(i)==32:
                j=j+i             
            #shift<0:
            #j=i.replace(i,chr(ord(i)-(abs(shift))))
            #coded+=j
    # Decode Section
else:
    for i in message:#range(len(message)):
        if 48 <=ord(i)<=57:
            NumericError=True        
        #print(i,ord(i))
        if 65 <= ord(i) <= 90 :
            if ord(i)+shift < 65:
                j=j+chr(ord(i)+shift+26)#i.replace(i,chr(ord(i)+shift)-28)        
            else: 
                j=j+chr(ord(i)+shift)#i.replace(i,chr(ord(i)+shift))
            #coded+=j
        
        elif 97 <= ord(i) <= 122 :
            if ord(i)+shift < 97:
                j=j+chr(ord(i)+shift+26)#i.replace(i,chr(ord(i)+shift)-28)        
            else: 
                j=j+chr(ord(i)+shift)#i.replace(i,chr(ord(i)+shift))   
        elif ord(i)==32:
                j=j+i                                  
            #shift<0:
            #j=i.replace(i,chr(ord(i)-(abs(shift))))
            #coded+=j
    # Decode Section        
if NumericError==True:
    print("You Use illegal Charachter!")
else:
    print(j)


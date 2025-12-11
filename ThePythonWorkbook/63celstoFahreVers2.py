celsius=[]
#celsius=[0,10,20,30,40,50,60,70,80,90,100]
j=0 
fahrenheit=[]
print("Celsius\tFahrenheit")
for i in range(0,100,10):
    celsius.append(i)
    F=(int(i) * 1.8) + 32
    fahrenheit.append(F)

    print(celsius[j],"\t",fahrenheit[j])
    j+=1    

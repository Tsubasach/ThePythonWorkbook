
'''while True:
    day=input("Enter day from 0-30:")
    if int(day)<30 and int(day)>0:
        break'''
    
day=input("The Day number should between 0-30: ")
while True:
    if day.isnumeric():
        if 0<int(day)<=30 :
            D=int(day)*86400
            break
        else:
            day=input("the number should between 0-30: ")
    else:
        day=input("the number should between 0-30:")
        
hour=input("Enter Hour from 0-12:")
while True:    
    if hour.isnumeric():
        if 0<int(hour)<=12:
            Ho=int(hour)*3600
            break
        else:
            H=input("the number should between 0-12:")
    else:
        H=input("the number should between 0-12:")  
        
minute=input("Enter Minute from 0-60:")
while True:
    if minute.isnumeric():
        if 0<int(minute)<=60:
            Mi=int(minute)*60
            break
        else:
            M=input("the number should between 0-60:")
    else:
        M=input("the number should between 0-60:")
second=input("Enter Second from 0-60:")
while True:
    if second.isnumeric():
        if 0<int(second)<=60:
            So=int(second)
            break
        else:
            S=input("the number should between 0-60:")
    else:
        S=input("the number should between 0-60:")

timeinSec=D+Ho+Mi+So
print(timeinSec)







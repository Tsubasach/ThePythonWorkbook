import calendar



mon=input("Enter Month: ")
day=input("Enter Day: ")


'''capr1=("22","23","24","25","26","27","28","29","30")
capr2=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
aqua1=range(20,30)
aqua2=range(1,18)
#months=calendar
#print(months)'''

months=("January","February","march","april","may","june","july","augeust","september","october","november","december")
dayss=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]


if len(mon) >= 3:
    mon[0].replace("j","J")
    if mon in ("January"):
       
        if 1 <= int(day) <=19:
                print("Capri")
    if mon in ("December"):
        if 22<= int(day) <=30:
                print("Capri")












    '''if mon in (months[0]) or mon in ("December"):
        x=dayss
        y=x.pop(19) + x.pop(19)

        if day in x:
            print("Its capricorn")
        else:
            print("Wrong(0)")
    else:
            print("Wrong(1)")
else:
            print("Wrong(2)")'''
    


#print(months[11])



#cap=range(1,30) - (20,21)
#x=[]
#y=x.pop(2) + x.pop(4) + x.pop(10)




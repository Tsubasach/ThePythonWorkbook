import calendar

user=input("input month:")

months={"January":1,"February":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}

#monthname=list(calendar.month_name)[1:]
#if user in months[user]:
    
lastday=calendar.monthrange(2025,int(months[user]))[1]
print(f"The last day of the month is: {lastday}")


#print(calendar.month(2025,2))
#while True:
#    if user.isalpha():
#        if user in monthname:
#            print()

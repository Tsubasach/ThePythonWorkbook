list=[4.95,9.95,14.95,19.95,24.95]
j=0
Newlist=[]
print("before\t After")
for i in list:
   After=round(i*0.6,2)
   Newlist.append(After)
   
   print(list[j],"\t", Newlist[j]) 
   j+=1



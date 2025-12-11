'''lis=[]
suma= 0
 
for i in range(3):
    num= int(input(f"Enter number {i + 1}:"))   
    if num >= 0:
        suma+=num
    lis.append(num)

lis.insert(0,num1)
lis.insert(1,num2)
lis.insert(2,num3)
print("Min is:",min(lis))
print("Max is:",max(lis))
sort=sorted(lis, key=int)
#print(min(sort))

middle=(suma)-min(sort)-max(sort)
print("Sorted is: ",sort)
print("The middle is: ",middle)'''



list1=[3,5,6]
a=0
if list1[0] > list1[1]:
    a=list1[0]
    list1[0]=list1[1]
    list1[1]=a
    
print(list1)
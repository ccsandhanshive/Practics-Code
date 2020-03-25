print("hii")
removeNumber=input()
array=input().split(",")
array2=[]
cnt=0
for i in array:
    if i not in removeNumber:
        array2.append(i)
for i in array2:
    if array2.count(i)==1:
        cnt+=1
print(cnt)        
        
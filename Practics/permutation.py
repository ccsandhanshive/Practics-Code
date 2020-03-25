InVal=[]
IntVal=input().split(",")
print(IntVal)
String=""
print("1")
for i in range(5,8,1):
    i=str(i)
    if i in InVal:
        print(i+"*")
        String+=i
        InVal.remove(i)
        print(String)
sumInt=sum(InVal)
cnt=0
for i in String:
    i=int(i,2)
    cnt+=i
    print(cnt)
print(sumInt+cnt)
    
    
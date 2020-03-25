n=5
processNo=['p1','p2','p3','p4','p5']
arrivalTime=[1,3,2,5,4]
burstTime=[7,2,5,8,6]
quatumTme=5
complitionTime=[]
watingTime=[]

for i in range(n):
    for j in range(n):
        print(arrivalTime[i],arrivalTime[j])
        if arrivalTime[i]>arrivalTime[j]:
            temp=arrivalTime[i]
            arrivalTime[i]=arrivalTime[j]
            arrivalTime=temp
            
            temp=processNo[i]
            processNo[i]=processNo[j]
            processNo[j]=temp
            
            temp=burstTime[i]
            burstTime[i]=burstTime[j]
            burstTime=temp
print(processNo)
print(arrivalTime)
print(burstTime)
    
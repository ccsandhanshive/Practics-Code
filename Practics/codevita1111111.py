N=int(input())
Array1=input().split(" ")
subarray1=[]
Array2=input().split(" ")
subarray2=[]


RemainingArrayWhichIsNotInArray=[]

Q=int(input())
Querys=[]
QInput=[]

if N<0 or N>(5*(10**3)):
    exit()
if Q<0 or Q>100000:
    exit()

for _ in range(Q):
    QInput=input().split(" ")
    Querys.append(QInput)
for i in Querys:
    subarray1=Array1[int(i[0])-1:int(i[1])]
    subarray2=Array2[int(i[2])-1:int(i[3])]
    for i1 in Array1:
        if (i1 not in subarray1) and (i1 not in subarray2 ):
            RemainingArrayWhichIsNotInArray.append(i1)
    for i1 in Array2:
        if (i1 not in subarray1) and (i1 not in subarray2 ):
            RemainingArrayWhichIsNotInArray.append(i1)
    RemainingArrayWhichIsNotInArray=set(RemainingArrayWhichIsNotInArray)
    print(len(RemainingArrayWhichIsNotInArray))
    RemainingArrayWhichIsNotInArray=[]        
    
    
noOfSwap=input()
noOfSwap=int(noOfSwap)
array=[]
array=input().split(",")
cnt=0
for i in range(len(array)):
    for j in range(i,len(array)):
        if array[i]>array[j] and cnt!=noOfSwap:
            get=array[i],array[j]
            array[j],array[i]=get
            cnt+=1
           
for i in array:
    print(i,end=" ")
array=input().split(",")
target=input().split(" ")
for i in target:
    sum1=0
    minsum=0
    index=0
    for j in array:
        i=int(i)
        j=int(j)
        sum1=i-j
        print("sum={}".format(sum1))
        if minsum==0:
            minsum=sum1
            if array.index(j) in array:
                index=array.index(j)
        elif minsum>abs(sum1):
            minsum=sum1
            index=array.index(j)
    print("{}".format(array.index(j)))
        

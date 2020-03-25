
n=int(input())

a=[]
for i in range(n):
    a1=int(input())
    a.append(a1)
    
for i in range(len(a)):
    for j in range(len(a)-1):
        temp=a[i]
        a[i]=a[j]
        a[j]=temp
        print(a)
        
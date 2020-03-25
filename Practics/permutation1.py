def permutation(a,l,r):
    if l==r:
        print(a)
    else:
        for i in range(l,r):
            temp=a[l]
            a[l]=a[i]
            a[i]=temp
            permutation(a,l+1,r)
            temp=a[l]
            a[l]=a[i]
            a[i]=temp
            
        
    



n=int(input())
a=[]
for _ in range(n):
    a1=int(input())
    a.append(a1)
permutation(a,0,n-1)
    
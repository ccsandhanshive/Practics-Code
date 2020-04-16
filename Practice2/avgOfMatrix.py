N,X=map(int,input().split())
arr=[]
for _ in range(X):
    arr1=list(map(float,input().split()))
    arr.append(arr1)
for marks in zip(*arr):
    print(sum(marks)/X)
    

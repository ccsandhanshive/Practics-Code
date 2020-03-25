X=int(input())
Y=int(input())
N=int(input())
n=0
cnt=0

while n<N:
    n+=N
    cnt+=1
    n-=Y
print(cnt)
        
        
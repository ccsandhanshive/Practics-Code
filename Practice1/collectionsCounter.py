from collections import Counter
x=int(input())
shoeList=list(map(int,input().split()))
n=int(input())
c=Counter(shoeList)
output=0
for _ in range(n):
    size,xi=map(int,input().split())
    if c[size]!=0:
        c[size]-=1
        output+=xi
print(output)


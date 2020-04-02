from itertools import combinations
s,k=map(str,input().split())
s=sorted(s)
for k1 in range(1,int(k)+1):
    arr=list(combinations(s,int(k1)))
    for i in arr:
        for j in i:
            print(j,end="")
        print()

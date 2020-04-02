from itertools import combinations_with_replacement
s,k=map(str,input().split())
s=sorted(s)
k=int(k)
for i in  combinations_with_replacement(s,k):
    for j in i:
        print(j,end="")
    print()
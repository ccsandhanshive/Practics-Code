from itertools import permutations
S,K=map(str,input().split())
arr=list(permutations(S,int(K)))
arr.sort()
for i in arr:
    for j in i:
        print(j,end="")
    print()
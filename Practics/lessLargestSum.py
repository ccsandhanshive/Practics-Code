from itertools import combinations
l=input().split()
k=int(input())
combo=combinations(l,2)
validCombo=[]
ans=0
for i in combo:
    val=0
    for j in i:
        val=int(val)+int(j)
    if int(val)<k and int(val)>ans:
        ans=int(val)
        pair=i
print(pair)
        

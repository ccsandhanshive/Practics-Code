from itertools import permutations
t=int(input())
for _ in range(t):
    a=input()
    blist=list(a)
    allPossible=permutations(blist,len(a))
    possible=[]
    for i in allPossible:
        value=list(i)
        fval=0
        for j in value:
            fval=(fval*10)+int(j)
        if fval>int(a):
            possible.append(fval)
    if len(possible)!=0:
        print(min(possible))
    else:
        print("not possible")

            
        
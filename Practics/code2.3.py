import itertools as i
t=int(input())
for _ in range(t):
    n=input()
    finalCount=0
    boxes=input().split(" ")
    while len(boxes) >1:
        combinations=i.combinations(boxes,2)
        #print(list(combinations))
        finalCombo=[]
        #print(len(finalCombo))
        for j in combinations:
            if len(finalCombo) is 0:
                finalCombo.append(j[0])
                finalCombo.append(j[1])
            else:
                #print("j={}".format(j))
                #print("finalCombo={}".format(finalCombo))
                if (j[0]+j[1])<(finalCombo[0]+finalCombo[1]):
                    finalCombo[0]=j[0]
                    finalCombo[1]=j[1]
        for k in finalCombo:
            if k in boxes:
                boxes.remove(k)
        finalCount+=int(finalCombo[0])+int(finalCombo[1])
        boxes.append(str(int(finalCombo[0])+int(finalCombo[1])))
        finalCombo.clear()
    print(finalCount)
    
'''2

4

1 2 3 4
19

5

1 2 3 4 5
33'''
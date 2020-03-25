dic=dict(input().split() for _ in range(3))
#print(dic)
for empnm in dic:
    #print(empnm)
    empid=dic[empnm]
    l=[]
    for i in empid:
        i=int(i)
        if i<=len(empnm):
            l.append(i)
    if len(l)!=0:        
        a=max(l)
        #print(a)
        str1=empnm[a-1]
    else:
        str1='X'
    print(str1,end="")        
t=int(input())
for i in range(t):
    l=int(input())
    flag=0
    s=[]
    r=[]
    s=input()
    s=list(s)
    scpy=s
    r=input()
    for j in range(len(s)):
        for k in range(len(s)):
            s[k],s[j]=s[j],s[k]
            #print("{}    {}".format("".join(s),r))
            if "".join(s)==r:
                if flag==0:
                    print("yes")
                    flag=1
            else:
                s=scpy
    if flag==0:
        print("no")
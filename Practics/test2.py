t=int(input())
s=[]
n=0
if t>0 and t<=3:
    for _ in range(t):
        n=int(input())
        if n<=200000 and n>=0:
            s=input().split(" ")
            for i in range(len(s)):
                if i>=0 and i<1000000000:
                    i=int(i)
                    s[i]=int(s[i])-1
for i in s:
    print(i,end=" ")
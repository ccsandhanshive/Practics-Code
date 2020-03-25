l=input().split()

maxcnt=0
cnt=0
for j in range(len(l)):
    cnt=0
    minval=0
    for i in l[j:]:
        #print(i,minval)
        if int(i)>int(minval):
            minval=i
            cnt=cnt+1;
         #   print("cnt={0}".format(cnt))
    if cnt>maxcnt:
        maxcnt=cnt
   # print(" ")
print(maxcnt)
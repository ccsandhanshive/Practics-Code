t=int(input())
flag=0
for k in range(t):
    N=int(input())
    for i in range(N):
        print(".",end="")
        for j in range(i,N):
            print(".",end="")
            if "4" not in str(i):
                if "4" not in str(j):
                    if i+j==N:
                        print()
                        print("Case #{}:{} {}".format(k,i,j))
                        flag=1
                        break
        if flag==1:
            flag=0
            break

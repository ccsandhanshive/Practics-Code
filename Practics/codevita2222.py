N,M=input().split(" ")
N=int(N)
M=int(M)
k=int(input())
res=[]
for _ in range(k):
    coor=input().split(" ")
    res.append(coor)
dist=int(input())
grid=[[0 for x in range(N)] for y in range(M)] 
pair=[]
#print(res)
for i in range(N):
    for j in range(M):
        pair=[str(i),str(j)]
        #print(pair)
    
        if pair in res:
               grid[i][j]="R"
        else:
               grid[i][j]="-"
print(grid)
        


    
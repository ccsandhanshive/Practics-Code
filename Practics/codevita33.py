def linking(element,ArrayList):
    if element in ArrayList:
        return True
    else:
        return False
N,M=input().split(" ")
M=int(M)
N=int(N)
array1=[0 for x in range(M)]
array2=[0 for x in range(M)]
city=[[0 for x in range(N)] for y in range(M)]
for i in range(M):
    array1[i],array2[i]=input().split(" ")     
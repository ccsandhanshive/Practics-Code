from itertools import product
A=map(int,input().split())
B=map(int,input().split())
for i in list(product(A,B)):
    print(i,end=" ")
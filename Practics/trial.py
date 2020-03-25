def findSub(numbers,s,min1,max1):
    #print(min1),print(max1)
    if sum(numbers[min1:max1])==s:
        #print("01")
        return min1+1,max1
    if max1+1<=len(numbers):
        #print("10")
        return findSub(numbers,s,min1,max1+1)
    elif min1+1<=len(numbers):
        #print("11")
        return findSub(numbers,s,min1+1,min1+2)
    else:
        #print("100")
        return -1
        
    
        
    
    
    
    
    
t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    numbers=list(map(int,input().split()))
    min1,max1=findSub(numbers,s,0,1)
    print(min1,end=" "),print(max1)
    
'''2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10'''
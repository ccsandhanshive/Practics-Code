global maximum
def checkCondition(A,B):
    if ((A&B)*2)<(A|B):
        return True
    else:
        return False

def _lis(arr,n):
    global maximum
    if n==1:
        return 1
    MaxEndingHere=1
    for i in range(1,n-1):
        res=_lis(arr,i)
        if arr[i+1]<arr[n-1] and res+1>MaxEndingHere and (checkCondition(arr[i],arr[i+1])):
            MaxEndingHere=res+1
    maximum=max(maximum,MaxEndingHere)
    return MaxEndingHere
def lis(arr):
    global maximum
    n=len(arr)
    maximum=1
    _lis(arr,n)
    return maximum
                


  

    
def solver(A):
    return lis(A)
            
            
    
def main():
    
    N=int(input())
    if 1<=N and N<=10:
        A=[None]*N
        for j in range(N):
            A[j]=int(input())
            
        result=solver(A)
        print(result)
if __name__=="__main__":
    main()
    
    #8
    #15
    #13
    #10
    #3
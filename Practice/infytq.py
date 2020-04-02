def checkCondition(A,B):
    if ((A&B)*2)<(A|B):
        return True
    else:
        return False
    
        
def solver(A):
    B=A.copy()
    for i in range(1,len(B)-1):
        if checkCondition(B[i],B[i+1]):
            print(A[i])
            print(A)
def main():
    N=int(input())
    A=[None]*N
    for j in range(N):
        A[j]=len(input())
        
    result=solver(A)
    print(result)
if __name__=="__main__":
    main()

def nCr(n, r): 
  
    return (fact(n) / (fact(r)  
                * fact(n - r))) 
  
# Returns factorial of n 
def fact(n): 
  
    res = 1
      
    for i in range(2, n+1): 
        res = res * i 
          
    return res 
  
# 
n,r=input().split(" ")
n=int(n)
r=int(r)
sum1=0
for i in range(0,r+1,2):
    sum1=sum1+nCr(n,i)
print(int(sum1))
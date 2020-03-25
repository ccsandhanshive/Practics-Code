from math import gcd as bltin_gcd

def coprime(a,b):
    return bltin_gcd(a,b)==1

n=int(input())
cnt=0
for i in range(n):
    if(coprime(i,n)):
        if i<=n:
            cnt=cnt+1
print(cnt)
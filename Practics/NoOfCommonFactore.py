def commonFactor(a,b):
    n=0
    for i in range(1, min(a, b)+1): 
        if a%i==b%i==0: 
            n+=1
    return n
inputString=input()
a,b=inputString.split(" ")
a=int(a);b=int(b)
if 1<=a and b<=(10**12):
    print(commonFactor(a,b))
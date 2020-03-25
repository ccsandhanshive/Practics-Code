def checkPrime(sum1):
    if sum1 > 1:
        for i in range(2,sum1):
            if (sum1 % i) == 0:
                return False
                break
    else:
        return False
    return True

   
    

a=input().split()
for i in range(len(a)):
    for j in range(i+1,len(a),1):
        sum1=abs(int(a[i])-int(a[j]))
        sum1=int(sum1)
        #print(sum1)
       # try:
        if checkPrime(sum1):
            print(a[i]+","+a[j])
        #except:
         #   print("divide by 0")
            

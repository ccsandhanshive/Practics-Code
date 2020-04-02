def rev(s):
    s1=""
    for i in s:
        s1=i+s1
    return s1
def digit_sum(n):
    sm=0
    while(n!=0):
        sm+=n%10
        n=n//10
    return sm
def getNumber(N,k):
    count=0
    for number in range(1,10001):
        if(len(str(number))==N):
            if(str(number)==rev(str(number))):
                if((digit_sum(number))%k==0):
                    count+=1
            elif(len(str(number))>N):
                break
    return count
print(getNumber(2,3))
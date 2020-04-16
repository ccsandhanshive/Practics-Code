upper=[]
lower=[]
even=[]
odd=[]
def divide(InputString):
    #print("0")
    if InputString.isalpha():
        #print("00")
        if InputString.isupper():
            #print("000")
            upper.append(InputString)
        else:
            #print("001")
            lower.append(InputString)
    else:
        #print("01")
        if int(InputString)%2==0:
            #print("010")
            even.append(InputString)
        else:
            #print("011")
            odd.append(InputString)
    return
for i in list(input()):
    divide(i)
upper.sort()
lower.sort()
even.sort()
odd.sort()
output=lower+upper+odd+even
for i in output:
    print(i,end="")



        

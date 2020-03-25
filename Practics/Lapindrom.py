def Palindrome(string):
    str1=""
    str2=""
    if len(string)%2!=0:
        for i in range(mid):
            str1+=string[i]
        for j in range(mid+1,len(string)):
            str2+=string[j]
    else:
        for i in range(mid):
            str1+=string[i]
        for j in range(mid,len(string)):
            str2+=string[j]
    return str1,str2

def RevPalindrom(string):
    str1=""
    str2=""
    if len(string)%2!=0:
        for i in range(mid):
            str1+=string[i]
        for j in reversed(range(mid+1,len(string))):
            str2+=string[j]
    else:
        for i in range(mid):
            str1+=string[i]
        for j in reversed(range(mid,len(string))):
            #print("j={}".format(j))
            str2+=string[j]
    return str1,str2
    
    

string=list(input())
str1=""
str2=""
mid=(len(string)//2)
print(mid)
str1,str2=Palindrome(string)
str3,str4=RevPalindrom(string)
    

if str1==str2 or str3==str4:
    print("yes")
else:
    print("No")



#print("str1{}".format(str1))
#print("str2{}".format(str2))
#print("str3{}".format(str3))
#print("str4{}".format(str4))

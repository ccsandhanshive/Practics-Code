
'''def getMissingVal(numbers):
    return ((max(numbers)*(max(numbers)+1))//2)-(sum(numbers))'''

def getMissingVal(numbers,count):
    ans=[]
    for i in range(1,count):
        if i not in numbers:
            ans.append(i)
    return ans
n=int(input())
for _ in range(n):
    numbers=input()
    count=int(input())
    numbers=numbers.split(",")
    for i in range(len(numbers)):
        numbers[i]=int(numbers[i])
    
    print(getMissingVal(numbers,count))
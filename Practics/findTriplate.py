def findTriplate(numbers):
    count=0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if (numbers[i]+numbers[j]) in numbers:
                count+=1
    if count==0:
        return -1
    return count
t=int(input())
for _ in range(t):
    n=input()
    numbers=list(map(int,input().split()))
    print(findTriplate(numbers))
















'''Example:
Input:
2
4
1 5 3 2
3
3 2 7
Output:
2
-1'''
t=int(input())
listp=[]
for _ in range(t):
    q=int(input())
    for _ in range(q):
        a=input().split()
        listp.append(a)
a_list=[]
output=[]
for i in listp:
    if i[0]=='A':
        a_list.append(int(i[1]))
    if i[0]=='I':
        for j in range (len(a_list)):
            a_list[j]=int(a_list[j])+int(i[1])
    if i[0]=='D':
        for j in range (len(a_list)):
            a_list[j]=int(a_list[j])-int(i[1])
    if i[0]=='P':
        output.append(i[1])
a_list.sort()
for i in output:
    if int(i)>=len(a_list):
        i=len(a_list)
    print(a_list[len(a_list)-int(i)])
        
'''1
10
A 10
A 15
A 20
I 10
A 22
D 5
A 27
P 3
P 2
P 5'''            
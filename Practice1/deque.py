from collections import deque
deq=deque()
for _ in range(int(input())):
    input1=list(input().split())
    if input1[0]=='append':
        deq.append(int(input1[1]))
    if input1[0]=='appendleft':
        deq.appendleft(int(input1[1]))
    if input1[0]=='pop':
        deq.pop()
    if input1[0]=='popleft':
        deq.popleft()
    input1=[]
for i in deq:
    print(i,end=" ")

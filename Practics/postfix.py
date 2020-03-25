l=input().split()
exp=list(l)
ope=['+','-','*','/','%']
stack=[]
for i in l:
    if i not in ope:
        stack.append(i)
    else:
        val1=stack.pop()
        val2=stack.pop()
        if i is '+':
            stack.append(int(val1)+int(val2))
        if i is '-':
            stack.append(int(val1)-int(val2))
        if i is '*':
            stack.append(int(val1)*int(val2))
        if i is '/':
            stack.append(int(val1)/int(val2))
        if i is '%':
            stack.append(int(val1)%int(val2))
print(stack)
string=input()
c,ab=string.split("||")
c=c.split("|")
ab=list(ab)
a=ab[len(ab)-1]
ab.pop()
#print(c)
#print(a)
#print(ab)

string1=input()
raw=list(string1)
#print(raw)
extended_positions=[]
for i in c:
    if int(i)>9:
        extended_positions.append(i)
#print(extended_positions)
ten_empty_positions=[None] * 10;
for i in extended_positions:
    for j in range(len(i)-1):
        ten_empty_positions[int(i[j])]=i[len(i)-1]
#print(ten_empty_positions)
for i in ab:
    ten_empty_positions[int(i)]=int(ten_empty_positions[int(i)])+10
#print(ten_empty_positions)
passIndex=[]
passIndex.append(a)
for i in range(len(ten_empty_positions)):
    if ten_empty_positions[i] is not None:
        ten_empty_positions[i]=int(ten_empty_positions[i])-int(a)
        a=ten_empty_positions[i]
        passIndex.append(a)
passIndex.pop()
#print(passIndex)
for i in passIndex:
    print(raw[int(i)],end="")        
    
'''
0|1|2|43|14|5|6|7|308|29||0149

*Acf$zd&T@
@@z$$'''
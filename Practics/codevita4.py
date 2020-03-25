array1=[1,1,2,5,5]
array2=[2,3,4,6,7]
visited=[]
MainRoute=[]
route=[]
    
def serchInKey(element):
    if element in array1:
        return True
    else:
        return False

for i in range(len(array1)):
    route.append(array1[i])
    #print("i ={}".format(array1[i]))
    j=array2[i]
    route.append(j)
    #print("j ={}".format(j))
    while serchInKey(j):
        index=array1.index(j)
        #print(index)
        j=array2[index]
        route.append(j)
        #print("-j ={}".format(j))
    MainRoute.append(route)
    route=[]
#print(MainRoute)
Main=[]
for i in range(len(MainRoute)):
    for j in range(len(MainRoute)):
        if any(x in MainRoute[i] for x in MainRoute[j]):
            MainRoute[i]+=MainRoute[j]
            MainRoute[i]=list(set(MainRoute[i]))
            #print(MainRoute)
for i in MainRoute:
    Main.append(str(i))
maxLen=0
MainRoute=[]
temp=[]
for i in Main:
    for j in i:
        if j.isdigit():
            temp.append(j)
    MainRoute.append(temp)
print(MainRoute)
print(maxLen)
    


        
        
    
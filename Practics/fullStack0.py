class tree:
    def __init__(self,val):
        self.data=val
        self.childs=[]
    def returnChild(self):
        return self.childs
    def createNewChild(self,child):
        self.childs.append(tree(child))
    




def createTree(parent,val):
    t=tree(val[0])
    for i in set(parent):
        t.createNewChild(i)
    for i in range(len(t.childs)):
        for j in range(len(parent)):
            if t.childs[i].data==parent[j]:
                t.childs[i].createNewChild(val[j+1])
    return t
    
def returnNoOfFactors(x):
    listOfFactors=[]
    if x==0:
        return 0
    else:
        for i in range(1,x+1):
            if x%i==0:
                listOfFactors.append(i)
        return len(listOfFactors)

def checkPrime(val):
    for i in range(2,val):
        if val%i==0:
            return False
    return True

def returnSpecialNode(tr,i):
    if checkPrime(tr.childs[i].data):
        return tr.childs[i].data
    else:
        return 0


def covertTreeIntoArray(tree):
    childsList=[]
    parentList=[]
    TreeList=[tree.data,]
    for i in range(len(tree.childs)):
        parentList=[int(tree.childs[i].data),]
        for j in range(len(tree.childs[i].childs)):
            childsList.append(int(tree.childs[i].childs[j].data))
        parentList.append(childsList)
        TreeList.append(parentList)
        parentList=[]
        childsList=[]
    return TreeList

def printSpecialNumber(Newtree):
    specialNode=0
    #print(type(Newtree))
    #print(type(specialNode))
    specialNumber=0
    if type(Newtree)==type(specialNode):
      # print("for ",Newtree)
       if checkPrime(Newtree):
            specialNode=Newtree
       if returnNoOfFactors(Newtree)!=0:
            specialNumber=returnNoOfFactors(Newtree)|specialNode
       else:
            specialNumber=0
    print(specialNumber,end=" ")


def solve(parent,val):
    '''print(type(val))
    val=list(val)
    for x in list(set(parent)):
        val.remove(x)'''
    tr=createTree(parent,val)
    Newtree=covertTreeIntoArray(tr)
    print(Newtree)
    for i in range(len(Newtree)-1):
       # print("step 1:")
        printSpecialNumber(Newtree[i])
        for j in range(len(Newtree[i+1])-1):
        #    print("step 2:")
            printSpecialNumber(Newtree[i+1][j])
            for k in range(len(Newtree[i+1][j+1])-1):
         #       print("step 3:")
                printSpecialNumber(Newtree[i+1][j+1][k])
        
    
    
        
    
    
    
    
    

    
    
    
    
    
        


no=5
val=[7,6,4,1,3]
parent=[1,1,3,3]
out_=solve(parent,val)
print(out_)
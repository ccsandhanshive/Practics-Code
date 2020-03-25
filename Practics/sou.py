import numpy as np
import pandas as pd

distr_table=pd.DataFrame({
        'X':[0,0,1,1],
        'Y':[1,2,1,2],
        'pr':[0.3,0.25,0.15,0.3]
        })
pr_in=0
table=np.zeros((len(distr_table.X),len(distr_table.Y)))
prList=[]

#print(table)
x=[]
y=[]
pr_in=0
for i in distr_table.pr:
    prList.append(i)
for i in distr_table.X:
    x.append(i)
for i in distr_table.Y:
    y.append(i)
for i in range(len(x)):
    for j in range(i,len(y)):
       table[y[i]][x[j]]=prList[pr_in]
       pr_in+=1
       break
    
#print(table)

table=pd.DataFrame(table)
#print(table)
table['total_Y']=table.sum(axis=1)
table['total_X']=table.sum()

#print(table)

#BoolMatrix=np.empty(len(table),len(table))
#print(len(table))















def independent(table,i,j):
    if table.iloc[j][i]==table.iloc[j][4]*table.iloc[j][5]:
        return True
    else:
        return False
    
    
    
    
    
    

def cov(table,i,j):#cov(table)
    return (int(i)-mouX(table,i,j))*(int(j)-mouY(table,i,j))
    #print(tempSum,end=" ")   
def mouX(table,i,j):
    return table.iloc[j][i]*table.iloc[j][4]
 

def mouY(table,i,j):
    return table.iloc[j][i]*table.iloc[j][5]
           
for i in table.columns:
        for j in table.index:
            if(i!='total_Y') and (i!='total_X'):
                print(cov(table,i,j),end=" ")
                
        print()
        
def corr(table,i,j):
    try:
        return cov(table,i,j)/(BetaX(table,i,j)*BetaY(table,i,j))
    except:
        pass
def BetaX(table,i,j):
    return table.iloc[j][4]*((j-mouX(table,i,j))**2)
def BetaY(table,i,j):
    return table.iloc[j][4]*((j-mouY(table,i,j))**2)

for i in range(len(table)):
    for j in range(len(table)):
        try:
            print(independent(table,i,j),end=" ")
            print(cov(table,i,j),end=" ")
            print(corr(table,i,j))
        except:
            pass
            
    print()       
     
'''
    2.corr(x,y)=cov(x,y)/OxOy
    
    3.Ox=for j=1 to m {
    pj(xj-ux)*(xj-ux)
    }
    4.Oy=for k=1 to l{
    Pk(yk-uy)*(yk-uy)
    }


def cov()'''

























'''class CheckIndependence:
    def __init__(self):
        self.version=1
        
    def check_independence(self,distr_table):
        pass'''
        

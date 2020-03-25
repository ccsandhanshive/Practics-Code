import numpy as np
import pandas as pd

distr_table=pd.DataFrame({
        'X':[0,0,1,1],
        'Y':[1,2,1,2],
        'pr':[0.3,0.25,0.15,0.3]
        })
pr_in=0
table=np.empty((len(distr_table.X),len(distr_table.Y)))
prList=[]


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
    

table=pd.DataFrame(table)
table['total_Y']=table.sum(axis=1)
table['total_X']=table.sum()
















def independent(table,i,j):
    if table.iloc[j][i]==table.iloc[j][4]*table.iloc[j][5]:
        return True
    else:
        return False
    
    
    
    
    
    

def cov(table,i,j):
    return (int(i)-mouX(table,i,j))*(int(j)-mouY(table,i,j))
     
def mouX(table,i,j):
    return table.iloc[j][i]*table.iloc[j][4]
 

def mouY(table,i,j):
    return table.iloc[j][i]*table.iloc[j][5]

        
def corr(table,i,j):
    try:
        return cov(table,i,j)/(BetaX(table,i,j)*BetaY(table,i,j))
    except:
        pass
def BetaX(table,i,j):
    return table.iloc[j][4]*((j-mouX(table,i,j))**2)
def BetaY(table,i,j):
    return table.iloc[j][4]*((j-mouY(table,i,j))**2)





def inde():
    are_independet=False
    cov1=0.0
    corr1=0.0
    for i in range(len(table)):
        for j in range(len(table)):
            try:
                are_independet+=independent(table,i,j)
                are_independet=bool(are_independet)
                cov1+=cov(table,i,j)
                corr1+=corr(table,i,j)
            except:
                pass
    return dict({'are_independet':are_independet,'cov':cov1,'corr':corr1})
print(inde())
     

























'''class CheckIndependence:
    def __init__(self):
        self.version=1
        
    def check_independence(self,distr_table):
        pass'''
        

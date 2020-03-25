import numpy as np
import pandas as pd

distr_table =pd.DataFrame({
        'X':[0,0,1,1],
        'Y':[1,2,1,2],
        'pr':[0.3,0.25,0.15,0.3]
        })


class CheckIndependence:
    def __init__(self):
        self.version=1
    def independent(self,table,i,j):
            print(table.iloc[j][3],end=" ")
            print(table.iloc[j][4])
            if table.iloc[i][j]==table.iloc[j][3]*table.iloc[j][4]:
                return True
            else:
                return False
        
    def check_independence(self,distr_table):
        self.pr_in=0
        table=[[ 0 for col in range(3)] for row in range(3)]
        self.prList=[]
        #print(table)
        self.x=[]
        self.y=[]
        self.pr_in=0
        for i in distr_table.pr:
            self.prList.append(i)
        for i in distr_table.X:
            self.x.append(i)
        for i in distr_table.Y:
            self.y.append(i)
        for i in range(len(self.x)):
            for j in range(i,len(self.y)):
                table[self.y[i]][self.x[j]]=self.prList[self.pr_in]
                self.pr_in+=1
                break
        #print(table)
        table=pd.DataFrame(table)
        table['total_Y']=table.sum(axis=1)
        table['total_X']=table.sum()
        print(table)
        self.are_independet=True
        self.cov1=0.0
        self.corr1=0.0
        print(len(table)-1)
        for i in range(len(table)):
            for j in range(len(table)):
                self.are_independet*=self.independent(table,i,j)
                #print(table.loc[j][i],end=" ")
                
                #print(self.independent(table,j,i))
                self.are_independet=bool(self.are_independet)
                self.cov1+=self.cov(table,i,j)
                self.corr1+=self.corr(table,i,j)
        return dict({'are_independet':self.are_independet,'cov':self.cov1,'corr':self.corr1})
    
    def cov(self,table,i,j):
        if (table.iloc[0][i]is not None)and (table.iloc[0][j]is not None):
            return (int(table.iloc[0][i])-self.mouX(table,i,j))*(int(table.iloc[0][j])-self.mouY(table,i,j))
        else:
            return 0
    def mouX(self,table,i,j):
        return table.iloc[j][i]*table.iloc[j][3]
 

    def mouY(self,table,i,j):
        return table.iloc[i][j]*table.iloc[j][4]
    
    def corr(self,table,i,j):
        return self.cov(table,i,j)/(self.BetaX(table,i,j)*self.BetaY(table,i,j))
    def BetaX(self,table,i,j):
        return table.iloc[j][4]*((j-self.mouX(table,i,j))**2)
    def BetaY(self,table,i,j):
        return table.iloc[j][4]*((j-self.mouY(table,i,j))**2)

o=CheckIndependence()
print(o.check_independence(distr_table))        
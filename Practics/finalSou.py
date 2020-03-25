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
        if self.table.iloc[j][i]==self.table.iloc[j][4]*self.table.iloc[j][5]:
            return True
        else:
            return False
        
    def check_independence(self,distr_table):
        self.pr_in=0
        self.table=np.empty((len(distr_table.X),len(distr_table.Y)))
        self.prList=[]

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
                self.table[self.y[i]][self.x[j]]=self.prList[self.pr_in]
                self.pr_in+=1
                break

        self.table=pd.DataFrame(self.table)
        self.table['total_Y']=self.table.sum(axis=1)
        self.table['total_X']=self.table.sum()
        
        self.are_independet=True
        self.cov1=0.0
        self.corr1=0.0
        for i in range(len(self.table)):
            for j in range(len(self.table)):
                try:
                    self.are_independet*=self.independent(self.table,i,j)
                    self.are_independet=bool(self.are_independet)
                    self.cov1+=self.cov(self.table,i,j)
                    self.corr1+=self.corr(self.table,i,j)
                except:
                    pass
        return dict({'are_independet':self.are_independet,'cov':self.cov1,'corr':self.corr1})
    
    def cov(self,table,i,j):
        return (int(i)-self.mouX(table,i,j))*(int(j)-self.mouY(table,i,j))
     
    def mouX(self,table,i,j):
        return table.iloc[j][i]*table.iloc[j][4]
 

    def mouY(self,table,i,j):
        return table.iloc[j][i]*table.iloc[j][5]
    
    def corr(self,table,i,j):
        try:
            return self.cov(table,i,j)/(self.BetaX(table,i,j)*self.BetaY(table,i,j))
        except:
            return 0.0
    def BetaX(self,table,i,j):
        return table.iloc[j][4]*((j-self.mouX(table,i,j))**2)
    def BetaY(self,table,i,j):
        return table.iloc[j][4]*((j-self.mouY(table,i,j))**2)

o=CheckIndependence()
print(o.check_independence(distr_table))        
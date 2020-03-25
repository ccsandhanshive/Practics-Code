import numpy as np
import pandas as pd
import math

distr_table =pd.DataFrame({
        'X':[0,0,1,1],
        'Y':[1,2,1,2],
        'pr':[0.30,0.25,0.15,0.30]
        })


class CheckIndependence:
    def __init__(self):
        self.version=1
    def independent(self,table,i,j):
        if table.iloc[i][j]>0:
            if table.iloc[i][j]==table.iloc[j][3]*table.iloc[j][4]:
                return 1
            else:
                print(table.iloc[i][j],end=" ")
                print(table.iloc[j][3]*table.iloc[j][4])
                return 0
        else:
            return 1
    def findIndependent(self,table):
        are_independet=True
        for i in range(len(table)):
            for j in range(len(table)):
                are_independet*=self.independent(table,i,j)
                
        return bool(are_independet)
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
        are_independet=self.findIndependent(table)
        are_independet=bool(are_independet)
        cov=self.cov(table)
        corr=self.corr(table)
        return dict({'are_independet':are_independet,'cov':cov,'corr':corr})
    
    def cov(self,table):
        cov=0
        for i in range(len(table)):
            if (table.iloc[0][i]>0):
                cov+=(int(table.iloc[0][i])-self.mouX(table))*(int(table.iloc[1][i])-self.mouY(table))
        return cov
    def mouX(self,table):
        xSum=0
        for i in table.total_X:
            if i>0:
                xSum+=i
        return xSum

    def mouY(self,table):
        ySum=0
        for i in table.total_Y:
         ySum+=i
        return ySum
    
    def corr(self,table):
        return self.cov(table)/(self.BetaX(table)*self.BetaY(table))
        
    def BetaX(self,table):
        betaSum=0
        for j in table.total_X:
            betaSum+=j-self.mouX(table)**2
        return math.sqrt(abs(betaSum))
    def BetaY(self,table):
        betaSum=0
        for j in table.total_Y:
            betaSum+=j-self.mouX(table)**2
        return math.sqrt(abs(betaSum))

o=CheckIndependence()
print(o.check_independence(distr_table))        
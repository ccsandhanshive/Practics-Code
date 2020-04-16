#!/bin/python3

import math
import os
import random
import re
import sys



#Enter your code here. Read input from STDIN. Print output to STDOUT
class Employee:
    def __init__(self,name,id,age,gender):
        self.name=name
        self.id=id
        self.age=age
        self.gender=gender
    
class Organisation:
    def __init__(self,name,ListOfStore):
        self.name=name
        self.ListOfStore=ListOfStore

    def addEmployee(self,name,id,age,gender):
        self.ListOfStore.append(Employee(name,id,age,gender))
    def getEmployeeCount(self):
        return len(self.ListOfStore)
    def findEmployeeAge(self,id):
        for i in self.ListOfStore:
            if id==i.id:
                return i.age
        return -1
    def countEmployees(self,age):
        count=0
        for i in self.ListOfStore:
            if age<i.age:
                count+=1
        return count



if __name__ == '__main__':
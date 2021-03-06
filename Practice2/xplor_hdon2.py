#!/bin/python3

import math
import os
import random
import re
import sys



#Enter your code here. Read input from STDIN. Print output to STDOUT
class Student:
    def __init__(self,roll,name,marks_list):
        self.roll=roll
        self.name=name
        self.marks_list=marks_list
    def calculate_percentage(self):
        return sum(self.marks_list)//len(self.marks_list)
    def find_grade(self):
        per=self.calculate_percentage()
        if per>=80:
            return 'A'
        elif per>=60 and per<80:
            return 'B'
        elif per>=40 and per<60:
            return 'C'
        elif per<40 :
            return 'F'

if __name__ == '__main__':
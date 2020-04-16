#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'checkCoPrimeExistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def countPrimeNumbers(numbers):
    count=0
    for no in numbers:
        for i in range(2,no):
            if no%i==0:
                break
        else:
            count+=1
    return count



if __name__ == '__main__':
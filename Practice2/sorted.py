#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr=sorted(arr,key=lambda x: x[k],reverse=0)  
    for ele in arr:
        for i in ele:
            print(i,end=" ")
        print()    
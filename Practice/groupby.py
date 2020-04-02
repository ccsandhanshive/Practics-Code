from itertools import groupby
s=input()

for i,j in groupby(s):
    print("({1}, {0})".format(i,len(list(j))),end=" ")

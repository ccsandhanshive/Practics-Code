from itertools import permutations
for _ in range(int(input())):
    for i in permutations(input()):
        print(''.join(i),end=" ")
    








'''Example:
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA 
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA

Explanation:
Testcase 1: Given string ABC has permutations in 6 forms as ABC, ACB, BAC, BCA, CAB and CBA .
 '''
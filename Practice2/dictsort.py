from collections import Counter,OrderedDict
inputString=input()
dictCount=Counter(inputString)

dictCount=sorted(dictCount.items(),key=lambda x:x[0])
dictCount=OrderedDict(dictCount)
dictCount=sorted(dictCount.items(),key=lambda x:x[1],reverse=1)
dictCount=OrderedDict(dictCount)
count=0
for i in dictCount:
    print("{0} {1}".format(i,dictCount[i]))
    count+=1
    if count==3:
        break
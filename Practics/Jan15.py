def count_words(InputString):
    count=dict()
    splittedInputString=InputString.split(" ")
    for word in splittedInputString:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count

def returnMax(InputString):
    count=count_words(InputString)
    maxVal=0
    maxword=""
    for word in count:
        if count[word]>maxVal:
            maxVal=count[word]
            maxword=word
    return maxword
print(count_words("hellow ram hellow shyam"))
print("------------------------")
print(returnMax("hellow ram hellow shyam"))
            
import sys

def strongestPalindrome(string):
    maxlen = 1
  
    start = 0
    length = len(string) 
  
    low = 0
    high = 0
    print("maxlen={0} start={1} length={2} low={3} high={4}".format(maxlen,start,length,low,high))
    for i in range(1, length):
        
        low = i - 1
        high = i 
        print("maxlen={0} start={1} length={2} low={3} high={4}".format(maxlen,start,length,low,high))
        while low >= 0 and high < length and string[low] == string[high]: 
            
            if high - low + 1 > maxlen: 
                start = low 
                maxlen = high - low + 1
                print("maxlen={0} start={1} length={2} low={3} high={4}".format(maxlen,start,length,low,high))
            low -= 1
            high += 1
            print("maxlen={0} start={1} length={2} low={3} high={4}".format(maxlen,start,length,low,high))
        print("maxlen={0} start={1} length={2} low={3} high={4}".format(maxlen,start,length,low,high))
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]: 
            
            if high - low + 1 > maxlen: 
                start = low 
                maxlen = high - low + 1
                print("maxlen={0} start={1} length={2} low={3} high={4}".format(maxlen,start,length,low,high))
            low -= 1
            high += 1
        print("maxlen={0} start={1} length={2} low={3} high={4}".format(maxlen,start,length,low,high))
        print (string[start:start + maxlen])
    print("maxlen={0} start={1} length={2} low={3} high={4}".format(maxlen,start,length,low,high))
    print (string[start:start + maxlen])
    
string = input()
strongestPalindrome(string)

def decomposite(number):#number=4444
    Asum=0
    Bsum=0
    for i in str(number):
        if i == "4":#4
            zeStr=""
            zero=(len(str(number))-1)-str(number).index(i)#zero=2
            for _ in range(zero):
                zeStr+="0"
            A="1"+zeStr#A=100
            B="1"+zeStr#B=100
            A=2*int(A)#A=200
            B=2*int(B)#B=200
            Asum+=A#Asum=2200
            Bsum+=B#Bsum=2200
        else:          #9
            zeStr=""
            zero=(len(str(number))-1)-str(number).index(i)#zero=2-0
            for _ in range(zero):
                zeStr+="0"
            A="1"+zeStr#A=100
            A=int(i)*int(A) #A=900
            Asum+=A        #Asum=900
    return Asum,Bsum
            
t=int(input())
for _ in range(t):
    number=int(input())
    A,B=decomposite(number)
    print("{} {}".format(A,B))
''' 	
Output
 
3
4
940
4444

  
Case #1: 2 2
Case #2: 852 88
Case #3: 667 3777'''
def ans(number):
    c=1
    A,B=0,0
    while(number!=0):
        rem=number%10
        if rem==4:
            A+=c*2
            B+=c*2
            c*=10
        else:
            A+=c*rem
            c*=10
        number//=10
    return A,B
        
t=int(input())
for t1 in range(t):
    number=int(input())
    A,B=ans(number)
    print("Case #{}: {} {}".format(t1,A,B))
'''Output
 
3
4
940
4444

  
Case #1: 2 2
Case #2: 852 88
Case #3: 667 3777'''
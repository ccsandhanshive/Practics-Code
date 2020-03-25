def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm 


def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
  
    return x 
def gcd(numbers):
    res=numbers[0]
    for i in range(1,len(numbers)-1):
       res=find_gcd(res,numbers[i])
    return res
def lcm(numbers):
    res=numbers[0]
    for i in range(1,len(numbers)-1):
       res=find_lcm(res,numbers[i])
    return res
N=int(input())
ans=0
name=""
for i in range(N):
    Q=input().split(" ")
   
    numbers=[]
    if Q[0] is not "A":
        name=Q[0]
        numbers=Q[1].split(",")
        ans=lcm(numbers)
        print("{}'s question is:{} ".format(name,numbers))
    else:
        name=Q[1]
        Mans=Q[2]
        print(ans)
        if(Mans==ans):
            print("Correct Answer")
            print("{}: 10points")

            
    

    
#Lines will be of two types either a Question Posing line or Answer Giving line
#Question posing line has to appear before any answer giving line
#Question Posing line starts with Player Name and Answer Giving line starts with 'A'
#Second line will be a Question posing line whose format is where Perfect Sets are depicted in the format <X1
#,X2,...Xn> where 2<=n<=7 and 1<=Xn<=100
#Third line must be an Answer Giving line which is the answer to the precedingQuestion Posing line. The format of the Answer Giving line is as follows :
#answer above can only be an integer number OR it will be a constant string "PASS"
#An integer number represents the value of the answer given by the Player
#If the Player does not know the answer she will "PASS" the question
'''Fourth line onwards, if they exist, will be alternating series of Question Posing and Answer Giving lines in case of Valid inputs
In case of any Invalid Question Posing line, requisite output must be printed for all previous Valid Question posing line(s).
Processing should stop at Invalid input line after printing required message in output. See output specifications and sample test cases to understand points 5) and 6) better


Output Format:
First line of output must reiterate the question in the following format < Player Name >'s question is : X1,X2,X3...,Xn>

Second line should be an evaluation of the first Answer Giving line of the input. The evaluation message will either be { Correct Answer or Wrong Answer}
If the answer
is correct, output, : 10points
is wrong, output, : 0points
is "PASS"-ed by the player,
output "Question is PASSed"
output "Answer is: " where correct_answer_value is the correct answer for the question passed by the player.
output ": 0points"
Overall points collected by players have to be tracked and output when all valid inputs are processed
If all inputs are valid, after processing all the inputs, the final output should be comprised of the following 4 lines
Output "Total Points:" on fourth last line
Output ": points" on 3rd last line, where Player1 is the one who first posed the question
Output ": points" on 2nd last line, where Player2 is the one who first answered the question
If there is a winner Output "Game Result: is winner" or "Game Result: Draw"
Print "Invalid Input" in case of invalid input or failing constraint


Constraints:
0 < N <= 10
Player Names are Case-sensitive
Number of inputs in a Question posing line will be 2<=n<=7 and 1<=Xn<=100
<X1 ,X2,X3...,Xn> can only be integers'''
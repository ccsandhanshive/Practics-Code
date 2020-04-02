/*Someone just won the Code Jam lottery, and we owe them N jamcoins! However, when we tried to print out an oversized check, we encountered a problem. The value of N, which is an integer, includes at least one digit that is a 4... and the 4 key on the keyboard of our oversized check printer is broken.

Fortunately, we have a workaround: we will send our winner two checks for positive integer amounts A and B, such that neither A nor B contains any digit that is a 4, and A + B = N. Please help us find any pair of values A and B that satisfy these conditions.

Input
The first line of the input gives the number of test cases, T. T test cases follow; each consists of one line with an integer N.

Output
For each test case, output one line containing Case #x: A B, where x is the test case number (starting from 1), and A and B are positive integers as described above.

It is guaranteed that at least one solution exists. If there are multiple solutions, you may output any one of them. (See "What if a test case has multiple correct solutions?" in the Competing section of the FAQ. This information about multiple solutions will not be explicitly stated in the remainder of the 2019 contest.)

Limits
1 ≤ T ≤ 100.
Time limit: 10 seconds per test set.
Memory limit: 1GB.
At least one of the digits of N is a 4.

Test set 1 (Visible)
1 < N < 105.

Test set 2 (Visible)
1 < N < 109.

Solving the first two test sets for this problem should get you a long way toward advancing. The third test set is worth only 1 extra point, for extra fun and bragging rights!

Test set 3 (Hidden)
1 < N < 10100.

Sample

Input 
 	
Output 
 
3
4
940
4444

  
Case #1: 2 2
Case #2: 852 88
Case #3: 667 3777*/

import java.io.*;
import java.util.Scanner;
class Solution111{
public static void main(String args[]){
Scanner sc=new Scanner(System.in);
int t=sc.nextInt();
for(int a=1;a<=t;a++){
int n1=sc.nextInt();
int n=n1;
int[] nArry=new int[String.valueOf(n1).length()];
for(int i=0;i<String.valueOf(n1).length();i++){
if(n>1){
    nArry[i]=n%10;
n=n/10;
}else
{
nArry[i]=n;
}
}
int flag=0,flag1=0;
int icpy=0,jcpy=0;
for(int i=0;i<=n1;i++){

    
for(int j=0;j<=n1;j++){


if(i+j==n1)
{flag=0;
    icpy=i;jcpy=j;
    for(int k=0;k<String.valueOf(i).length();k++){
    for(int l=0;l<String.valueOf(n1).length();l++){
    if((icpy%10)==nArry[l])
    {    flag=1;
    
  break;
    }
    
 
    }
    icpy=icpy/10;
    }
    for(int k=0;k<String.valueOf(j).length();k++){
    for(int l=0;l<String.valueOf(n1).length();l++){
    if((jcpy%10)==nArry[l]){
    
    flag=1;
    

   break;
    }
    
    }
     jcpy=jcpy/10;
    }
if(flag==0)
{
System.out.println("Case #"+a+": "+i+" "+j);
flag1=1;
break;

}

}




}
    if(flag1==1)
        break;
}


}}
}
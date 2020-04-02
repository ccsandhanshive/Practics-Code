/*Some prime numbers can be expressed as Sum of other consecutive prime numbers.
For example

5 = 2 + 3
17 = 2 + 3 + 5 + 7
41 = 2 + 3 + 5 + 7 + 11 + 13

Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.

Write code to find out number of prime numbers that satisfy the above mentioned property in a given range.

Input Format:

First line contains a number N
Output Format:

Print the total number of all such prime numbers which are less than or equal to N.
Constraints:
1. 2

Sample Input and Output


SNo.	Input	Output	Comment
1	20	2	
(Below 20, there are 2 such numbers: 5 and 17).
5=2+3
17=2+3+5+7
2	15	1	*/
import java.util.Scanner;


public class prime {
public static void main(String args[]){
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int m=n;
int a[]= new int[n+1];int p=2;
for(int i=0;i<=n;i++){
  a[i]=i;
   
}

for(p=2;p*p<=n;p++){
    if(a[p]!=0){
    for(int i=p*2;i<=n;i+=p){
        a[i]=0;
    }
    }
}

int sum=5,count=0;
for(int j=5;j<=n;j=j+2){
    if((a[j]!=0&&a[j]==sum)||(a[j]==-1)){
        count++;
    }
    if((a[j]!=0)||(a[j]==-1)){
    sum=sum+j;}
    if(sum<n+1){
    if(a[sum]!=0){
            a[sum]=-1;
        }
    }
}
System.out.println(count);
}    
}

/*You are given N coins with values from 1 to N. You have exactly one coin of each denomination. You need to pay M hackos to the shubham. Find the minimum number of coins using which you can pay the shubham.

Input Format

Input consists of 2 space seperated integers N(the number of coins) and M(the hackos that you need to pay to the shubham).

Constraints

1<=N,M<=10000

Output Format

Output a single value equal to the minimum number of coins required to pay the entire hackos to the shubham. If it is impossible to pay the shubham with the hackos you have,then print -1.

Sample Input 0

2 3
Sample Output 0

2
Explanation 0

The problem boils down to finding whether it is possible to represent M as a sum of one or more coins using the minimum number of coins. So we start from the denomination N and go down till 1 and cumulatively take the sum and check if the sum is greater than or equal to M and we count the number of coins we took till now and break. So we get the minimum number of coins required to get the sum M and if the sum is less than M when we reach 1 then print -1.*/
import static java.lang.Math.ceil;
import static java.lang.Math.round;
import java.util.Scanner;


public class NewClass1 {
public static void main(String args[]){
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int m=sc.nextInt();
int sum=0,c=0;
for(int i=n;i>0;i--){
if(sum>=m){
break;
}else{
sum=sum+i;
c++;
}

}
if(sum<m){
    System.out.println("-1");
}else{
System.out.println(c);
}
}}

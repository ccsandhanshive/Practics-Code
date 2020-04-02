/*Problem Description
There are two banks; Bank A and Bank B. Their interest rates vary. You have received offers from both bank in terms of annual rate of interest, tenure and variations of rate of interest over the entire tenure.
You have to choose the offer which costs you least interest and reject the other.
Do the computation and make a wise choice.
The loan repayment happens at a monthly frequency and Equated Monthly Installment (EMI) is calculated using the formula given below :
EMI = loanAmount * monthlyInterestRate /
( 1 - 1 / (1 + monthlyInterestRate)^(numberOfYears * 12))

Constraints
1 <= P <= 1000000
1 <=T <= 50
1<= N1 <= 30
1<= N2 <= 30

Input Format
First line : P – principal (Loan Amount)
Second line : T – Total Tenure (in years).
Third Line : N1 is number of slabs of interest rates for a given period by Bank A. First slab starts from first year and second slab starts from end of first slab and so on.
Next N1 line will contain the interest rate and their period.
After N1 lines we will receive N2 viz. the number of slabs offered by second bank.
Next N2 lines are number of slabs of interest rates for a given period by Bank B. First slab starts from first year and second slab starts from end of first slab and so on.
The period and rate will be delimited by single white space.

Output
Your decision – either Bank A or Bank B.

Explanation
Example 1
Input
10000
20
3
5 9.5
10 9.6
5 8.5
3
10 6.9
5 8.5
5 7.9
Output
Bank B
Example 2
Input
500000
26
3
13 9.5
3 6.9
10 5.6
3
14 8.5
6 7.4
6 9.6
Output
Bank B*/








import java.io.*;
import java.util.Scanner;
import java.math.*;
class Solution{
public static void main(String args[]){

 Scanner sc=new Scanner(System.in);
 float loan_amt=sc.nextInt();
 double total_year=sc.nextDouble();
 int slabA=sc.nextInt();
 
 float peroidA[]=new float[slabA];
 float irA[]=new float[slabA];
 for(int i=0;i<slabA;i++){
 peroidA[i]=sc.nextFloat();  irA[i]=sc.nextFloat();
 }
 int slabB=sc.nextInt();
 
 float peroidB[]=new float[slabB];
 float irB[]=new float[slabB];
 for(int i=0;i<slabB;i++){
 peroidB[i]=sc.nextFloat();  irB[i]=sc.nextFloat();
 }

//double MonthlyInterestRateB=((((irb/loan_amt)/12)*100)*100);
double MonthlyInterestRateA[]=new double[slabA];
double emiA=0;
for(int i=0;i<slabA;i++){
//ira=ira+irA[i];
 MonthlyInterestRateA[i]=((((irA[i]/loan_amt)/12)*100)*100)/peroidA[i];
emiA=emiA+(loan_amt*MonthlyInterestRateA[i]/ ( 1-1/java.lang.Math.pow ( ( 1+MonthlyInterestRateA[i] ),( peroidA[i]*(double)12 ) ) ));
 
 }
double MonthlyInterestRateB[]=new double[slabB];
double emiB=0;
for(int i=0;i<slabA;i++){
//ira=ira+irA[i];
 MonthlyInterestRateB[i]=((((irB[i]/loan_amt)/12)*100)*100)/peroidB[i];
emiB=emiB+(loan_amt*MonthlyInterestRateB[i]/ ( 1-1/java.lang.Math.pow ( ( 1+MonthlyInterestRateB[i] ),( peroidB[i]*(double)12 ) ) ));
 
 } 
if(emiA<emiB){
System.out.println("Bank A");
}else
{
System.out.println("Bank B");
}









}

}
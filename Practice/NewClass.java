/*You need to write a program to accept input in the format specified, and produce output as specified. The program will be run against a number of test cases (2 public, given as examples, and the others private (which will not be known to you). The performance of the program (correctness of output and time taken to execute) against the test cases will be used to evaluate.
Max Square Sum Given a square array of size N x N where each cell is filled with a number between -9 and 9. A sub square of size k is any set of k contiguous columns and k contiguous rows. For any sub square, the sum of elements in its cells is called a sub square sum. Given the N x N square, write a program to find the maximum sub square sum. Note that a 1 x 1 square (k=1) is not considered a sub square) Input N, giving the size of the square The next N rows each contain N space separated integers giving the values of the cells in the rows of the square, left to right Output One integer, the maximum sub square sum Constraints N <= 1000 Example 1 Input
4
2 -8 4 -6
7 1 -5 3
-9 7 6 5
8 3 2 -4
Page | viii
Output 20 Explanation The 2 by 2 square sums are 2 -8 -4 6 9 9 9 18 9 The 3 by 3 square sums are 5 7 20 18 And the 4 by 4 square sum is 16. Hence the maximum sub square sum is 20.
Example 2 Input 3 1 1 0 1 2 2 3 0 4 Output 14 Explanation As all the entries are non-negative, the 3 by 3 sub square (which has a sum of 14) is the maximum*/
import java.util.Scanner;

class NewClass{
public static void main(String args[]){
Scanner sc=new Scanner(System.in);

int n=sc.nextInt();
int array[][]=new int[n][n];
int k=2;
for(int a=0;a<n;a++){
    for(int b=0;b<n;b++){
        array[a][b]=sc.nextInt();
    
    
    
    }



}




int sum=0,mainsum=0,c=0;
while(k<=n){

for(int i=0;i<n;i++){
   // System.out.println("for i="+i+";i<"+n+";i++");
    for(int j=0;j<n;j++){
   // System.out.println("for j="+j+";j<"+n+";i++");   
        for(int i1=i;i1<k+i;i1++){
           // System.out.println("for i1="+i1+";i1<"+n+";1i++");
            for(int j1=j;j1<k+j;j1++){
             //   System.out.println("for j1="+j1+";j1<"+n+";j1++");
                // System.out.println("if("+i1+"<"+n+"&&"+j1+"<"+n+")");
                if(i1<n&&j1<n){
                  // System.out.println("array["+i1+"]["+j1+"]="+array[i][j]);
                //System.out.println("sum="+sum+"+"+array[i1][j1]);
                    sum=sum+array[i1][j1];
                
                c++;
                //System.out.println("c="+c);
                }
            
            
            
            
            }
        
        
        
        
        }
    if(sum>mainsum&&c==(k*k)){
    //System.out.println(sum+">"+mainsum+"&&"+c+"=="+(k*k));
        mainsum=sum;
    //System.out.println("mainsum="+mainsum);
    }
    sum=0;c=0;
    
    
    }





}k++;
}
System.out.println(mainsum);
}

}
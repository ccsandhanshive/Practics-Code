import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static long fact(long number){
       long fact=1;
        for(int i=1;i<=number;i++){
            fact=fact*i;
        }
        return fact;
    }
    public static void main(String args[] ) throws Exception {
        Scanner sc=new Scanner(System.in);
        for(int i=0;i<5;i++){
            long number=sc.nextInt();
            System.out.println(fact(number));
        }
    }
    
   
}
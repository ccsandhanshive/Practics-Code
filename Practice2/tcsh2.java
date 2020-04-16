import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String args[] ) throws Exception {
        Scanner sc=new Scanner(System.in);
        String str=sc.next();
        char strList[]=new char[str.length()];
        strList=str.toCharArray();
        char min=strList[0];
        for(char i:strList){
            if((int)i<(int)min){
                min=i;
            }
        }
        System.out.println((char)min);
    }
}
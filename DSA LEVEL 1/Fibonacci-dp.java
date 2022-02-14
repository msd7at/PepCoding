import java.io.*;
import java.util.*;

public class Main{

public static void main(String[] args) throws Exception {
    // write your code here
    Scanner sc = new Scanner(System.in);
    int n =sc.nextInt();
    int f =0;
    int s=1;
    int t= n==0? 0:1;  
    for (int i=2;i<n+1;i++){

        t= s+f;
        f=s;
        s= t ;

    }
    System.out.println(t);

 }

}

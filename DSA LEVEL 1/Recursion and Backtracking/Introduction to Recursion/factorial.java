import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int ans= factorial(n);
        System.out.println(ans);
    }

    public static int factorial(int n){
        if (n==0){
            return 1;
        }
        
        return n*factorial(n-1);
    }

}

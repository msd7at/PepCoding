import java.util.*;

public class Main {

    // ~~~~~~~~~~~~~~~~User Section~~~~~~~~~~~
    public static int maximumProduct(int[] arr) {
        // write your code here
        int max1=Integer.MIN_VALUE;
        int max2=max1;
        int max3= max2;
        
        int min1= Integer.MAX_VALUE;
        int min2=min1;
        
        for (int i: arr){
            if (i>= max1){
                max3=max2;
                max2=max1;
                max1=i;
            }else if(i>=max2){
                max3=max2;
                max2=i;
            }else if(i>=max3){
                max3=i;
            }
            
            
            if (i<=min1){
                min2=min1;
                min1=i;
            }else if(i<=min2){
                min2=i;
            }
            
        }
        return Math.max(min1*min2*max1,max1*max2*max3);
    }

    // ~~~~~~~~~~~~~~~~Input Management~~~~~~~~~~~
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[] arr = new int[n];

        for(int i = 0; i < n; i++) {
            arr[i] = scn.nextInt();
        }

        int prod = maximumProduct(arr);
        System.out.println(prod);
    }
}

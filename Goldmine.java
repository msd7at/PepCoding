import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        // write your code here

        		Scanner scn = new Scanner(System.in);
		int n = scn.nextInt();
		int m = scn.nextInt();

		int[][] arr = new int[n][m];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				arr[i][j] = scn.nextInt();

			}
		}

		int dp[][] = new int[n][m];
		// int m = scn.nextInt();
//		printTargetSumSubsets(arr, 0, "", 0, m);

			//col
		for (int i = 0; i < m; i++) {
			//row
			for (int j = 0; j < n; j++) {
				if (i ==0) {
					dp[j][i] =  arr[j][i];
				}
				else if (j==0) {
					dp[j][i] = Math.max(dp[j][i-1],dp[j+1][i-1]) + arr[j][i];
				}
				else if (j==n-1) {
					dp[j][i] =Math.max(dp[j][i-1],dp[j-1][i-1])+ arr[j][i];
				}
				else {
					dp[j][i] = arr[j][i] + Math.max(dp[j][i-1],Math.max(dp[j-1][i-1], dp[j+1][i-1]));
					
				}
			}
		}
		int ans =00000;
		for (int i=0;i<n;i++) {
			ans = Math.max(ans, dp[i][m-1]);
		}

		System.out.println(ans);
    }

}

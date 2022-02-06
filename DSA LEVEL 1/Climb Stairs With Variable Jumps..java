// package com.leet;

import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		Scanner scn = new Scanner(System.in);
		int n = scn.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = scn.nextInt();
		}
		int paths = countPaths(arr, 0, n);
		System.out.println(paths);
		scn.close();
	}

	public static int countPaths(int[] arr, int index, int len) {

		int[] dp = new int[len + 1];
		dp[len ] = 1;
		for (int i = len - 1; i >= 0; i--) {
			for (int j =1; j<= arr[i] & j + i <= len; j++) {
					dp[i] += dp[i+j];
			}
		}
		
		return dp[0];
	
    }
}

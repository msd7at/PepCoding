import java.io.*;
import java.util.*;

public class Main {

public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}

		int x = Integer.parseInt(br.readLine());
		int ans=firstIndex(arr, 0, x);
		
		System.out.println(ans);

	}

	public static int firstIndex(int[] arr, int idx, int x) {

		if (idx == arr.length) {
			return -1;
		}

		else if (arr[idx] == x) {
			return idx;
		}
		return (firstIndex(arr, idx+1, x));
		

	}

}

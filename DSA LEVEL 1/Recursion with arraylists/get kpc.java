import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		int n = Integer.parseInt(br.readLine());
//		int[] arr = new int[n];
//		for (int i = 0; i < n; i++) {
//			arr[i] = Integer.parseInt(br.readLine());
//		}
//
//		int x = Integer.parseInt(br.readLine());
//		int ans=firstIndex(arr, 0, x);
//		
//		System.out.println(ans);
//		displayArr(arr,0);

		String str = br.readLine();
		ArrayList<String> ans = getKPC(str);
		System.out.println(ans);

	}

	static String[] arr = { ".;", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tu", "vwx", "yz" };

	public static ArrayList<String> getKPC(String str) {
		
		if (str.length()==0) {
			ArrayList<String> br = new ArrayList<>();
			br.add("");
			return br;
		}

		char ch = str.charAt(0);
		String ros = str.substring(1);

		ArrayList<String> rres = getKPC(ros);

		ArrayList<String> mres = new ArrayList<String>();

		String charCode = arr[ ch-'0'];

		for (int i = 0; i < charCode.length(); i++) {
			char chcode = charCode.charAt(i);
			for (String res : rres) {

				mres.add(chcode + res);
			}

		}

		return mres;
	}


}

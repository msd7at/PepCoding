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
		ArrayList<String> ans = gss(str);
		System.out.println(ans);

	}
	public static ArrayList<String> gss(String str) {
		
		if (str.length() == 0) {
			ArrayList<String> te= new ArrayList<>();
			te.add("");
			return te;
		}
		
		Character f= str.charAt(0);
		String ros = str.substring(1);
		ArrayList<String> rres = gss(ros);
		ArrayList<String> MM = new ArrayList<>();
		
		for (String jj : rres) {
			MM.add(""+jj);
//			MM.add(f+jj);
			
			
		}
		for (String jj : rres) {
//			MM.add(""+jj);
			MM.add(f+jj);
			
			
		}
//		System.out.println(MM+"====="+str);
        return MM;
    }


}

import java.util.*;

public class Main {
	// ~~~~~~~~~~~~~~User Section~~~~~~~~~~~~
	public static String reverseVowels(String s) {
		// write your code here
		char[] ar = s.toCharArray();

		int l = 0, r = ar.length - 1;

		while (l < r) {
			while (l<r && !isVowel(ar[l]) ) {
				l++;
			}
			
			
			while (l<r && !isVowel(ar[r]) ) {
				r--;
			}
			
			char a=ar[l];
			ar[l]=ar[r];
			ar[r]=a;
			
			l++;
			r--;
		}
		
		String o="";
		for (char h:ar){
		    o+=h;
		}
		return o;
	}
	
	public static boolean isVowel(char i) {
		if (i == 'a' || i == 'A' || i == 'e' || i == 'E' || i == 'i' ||
				i == 'u' || i == 'U' || i == 'o' || i == 'O' || i == 'I' ) {
			return true;
		}
		return false;
	}

	// ~~~~~~~~~~~~Input Management~~~~~~~~~~
	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		String str = scn.nextLine();

		String res = reverseVowels(str);
		System.out.println(res);
	}
}

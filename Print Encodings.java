

import java.io.*;
import java.util.*;

public class Main {

   	public static void main(String[] args) throws Exception {

		Scanner sc = new Scanner(System.in);
		String st = sc.next();
//		
		printEncodings(st, "");
		;

	}

	public static void printEncodings(String str, String ans) {

		if (str.length() == 0) {
			System.out.println(ans);
			return;
		}
		char first = str.charAt(0);
		if (first == '0') {
			return;
		}
//		int INt=((int)first);
//		System.out.println(INt);
		printEncodings(str.substring(1), ans + (char) ((int) first + 48));
		if ('1' == first || '2' == first) {
			if (str.length() > 1) {
//				int INt=(Integer.parseInt((str.substring(0, 2))) + 96);
//				System.out.println(str.substring(0, 2)+"  "+INt+ "  "+Integer.parseInt((str.substring(0, 2))));
				printEncodings(str.substring(2), ans + (char) (Integer.parseInt((str.substring(0, 2))) + 96));
			}
		}

	}

}

import java.util.Scanner;

public class Main {

	public static int max(int[] a) {
		// Write your code here.
		int ans = Integer.MIN_VALUE;
		int pr = 1;
		for (int i = 0; i < a.length; i++) {
			pr = pr * a[i];
			ans = Math.max(ans, pr);
			if (pr == 0) {
				pr = 1;
			}

		}
		pr = 1;
		for (int i = a.length - 1; i >= 0; i--) {
			pr = pr * a[i];
			ans = Math.max(ans, pr);
			if (pr == 0) {
				pr = 1;
			}

		}
		return ans;
	}

	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int[] a = new int[n];
		for (int i = 0; i < a.length; i++) {
			a[i] = s.nextInt();
		}
		System.out.println(max(a));

	}

}

package projectEuler;

import java.util.Date;

public class Multiples_3_5 {

	public static void main(String[] args) {
		long start = new Date().getTime();
		int sum = 0;
		for (int mult = 3; mult < 1000; mult += 3) {
			sum+= mult;
		}
		for (int mult = 5; mult < 1000; mult += 5) {
			if (mult % 3 != 0) {
				sum+= mult;
			}
		}
		long delta = new Date().getTime() - start;
		System.err.println("sum: " + sum + "; time: " + delta);
		
		start = new Date().getTime();
		sum = 0;
		for (int mult = 3; mult < 1000; mult++) {
			if (mult % 3 == 0 || mult % 5 == 0) {
				sum+= mult;
			}
		}
		
		delta = new Date().getTime() - start;
		System.err.println("sum: " + sum + "; time: " + delta);
	}
	
	//Results when upper limit is 1e9 instead of 1000
	//sum: 631780268; time: 827
	//sum: 631780268; time: 2178

}

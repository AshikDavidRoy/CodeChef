package Sept_29_2022;

import java.io.*;
import java.util.Scanner;

public class Reach_the_Target {

	public static void main(String[] args) throws IOException {
		BufferedReader BufferedReader = new BufferedReader(new InputStreamReader(System.in));
		Scanner scanner = new Scanner(System.in);
		int X;// Team A Score
		int Y;// Team B current Score
		int T = scanner.nextInt();
		int num[] = new int[10];
		String[] strNums;

		for (int i = 0; i < T; i++) 
		{
			strNums = BufferedReader.readLine().split(" ");

			for (int j = 0; j < strNums.length; j++) 
			{
				num[j] = Integer.parseInt(strNums[j]);
			}

			X = num[0];
			Y = num[1];
			
			int Score= X-Y;
			
			if (0<Score) {
				System.out.println(""+Score);
			}
			
			else if (Score==0) {
				System.out.println(""+Score);
			}
			
			else {
				System.out.println("Team B wins");
			}
		}
		BufferedReader.close();
	}

}

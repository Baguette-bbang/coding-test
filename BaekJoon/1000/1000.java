// import java.util.Scanner;
// public class Main{

// 	public static void main(String[] args) {
// 		Scanner scan = new Scanner(System.in);
// 		int A,B;
// 		A=scan.nextInt();
// 		B=scan.nextInt();
		
// 		System.out.println(A+B);
// 	}
// }
import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		br.close();
		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());
		
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		bw.write(String.valueOf(a + b));
		bw.flush();
		bw.close();
	}
}
package 그리디;
import java.io.*;
import java.util.*;

class Main {
	static int N,K;
	static int sum=0;
	static int[] arr;
	static int[] distance;

	public static void main(String[] args) throws IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		K = Integer.parseInt(br.readLine());

		StringTokenizer st=new StringTokenizer(br.readLine());

		arr= new int[N];
		distance=new int[N-1];

		//1. 입력
		for (int i=0;i<N;i++)
			arr[i]=Integer.parseInt(st.nextToken());

		//2. 센서 오름차순 후 간격 구해서 오름차순
		Arrays.sort(arr);
		for (int i=0;i<N-1;i++)
			distance[i]=arr[i+1]-arr[i];
		Arrays.sort(distance);

		//3. 차이 큰 K-1 개 남겨두고 앞까지 더하기
		for (int i=0;i<N-K;i++)
			sum+=distance[i];

		//4. 출력
		System.out.println(sum);
	}
}
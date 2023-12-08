import java.io.*;
import java.util.*;

//13458번 시험 감독
public class 시험_감독 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        long answer = 0; //int 범위(20억) 넘을 수 있으니 long 타입

        answer += n; //총 감독 최소 시험장 개수만큼

        for (int i = 0; i < n; i++) {
            arr[i] -= b;     //총 감독 학생수 제외 남은 학생 인원 
            if (arr[i] <= 0) continue;
            answer += arr[i] / c;
            if (arr[i] % c != 0) { // 나머지 있으면 부감독 추가
                answer++;
            }
        }
        System.out.println(answer);
    }
}
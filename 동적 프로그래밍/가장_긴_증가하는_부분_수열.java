import java.io.*;
import java.util.*;
//11053번 가장 긴 증가하는 부분 수열
public class 가장_긴_증가하는_부분_수열 {
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int n= Integer.parseInt(br.readLine());
        int[] a= new int[n];
        int[] dp= new int[n];

        StringTokenizer st=new StringTokenizer(br.readLine());
        for (int i=0;i<n;i++){
            a[i]=Integer.parseInt(st.nextToken());
            dp[i]=1;
        }
            
        int max=1;
        for (int i=0;i<n;i++){
            for (int j=0;j<i;j++){
                //i번째 숫자가 1~i-1번째 앞 숫자들 보다 클 때
                if (a[i]>a[j]) dp[i]=Math.max(dp[i], dp[j]+1);
            }
            max=Math.max(max,dp[i]);
        }

        System.out.println(max);
    }
}
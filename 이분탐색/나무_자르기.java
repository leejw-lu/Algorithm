package 이분탐색;
import java.io.*;
import java.util.*;
//2805번 나무 자르기
public class 나무_자르기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        int n= Integer.parseInt(st.nextToken());
        int m= Integer.parseInt(st.nextToken());
        int[] arr= new int[n];
        int left=0;     //최소 높이
        int right=-1;   //최대 높이

        st= new StringTokenizer(br.readLine());
        for (int i=0;i<n;i++){
            arr[i]=Integer.parseInt(st.nextToken());
            right=Math.max(right,arr[i]);
        }

        while(left<=right){
            int mid= (left+right)/2;
            long sum=0;

            for (int i=0;i<n;i++){
                if (arr[i]>mid){
                    sum+=(arr[i]-mid);
                }
            }
            if (sum>=m) left=mid+1;
            else right=mid-1;
        }

        System.out.println(right);
    }
}

package 이분탐색;

import java.io.*;
import java.util.*;
//2512번 예산
public class 예산 {
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));

        int n= Integer.parseInt(br.readLine());
        int[] arr=new int[n];
        int left=0;     //최소 예산
        int right=-1;   //최대 예산

        StringTokenizer st= new StringTokenizer(br.readLine());
        for (int i=0;i<n;i++){
            arr[i]=Integer.parseInt(st.nextToken());
            right=Math.max(right, arr[i]);
        }
        int tatolCost=Integer.parseInt(br.readLine());
        //파라메트릭 서치로 꼭 정렬될 필욘X
        while (left<=right){
            int mid= (left+right)/2;
            int sum=0;
            for (int i=0;i<n;i++){
                if (arr[i]>mid) sum+=mid;   //세금 낼 수 있는 지방
                else sum+=arr[i];   //못내는 지방은 가진 돈 모두
            }
            if (sum<=tatolCost) left=mid+1; //국가예산 안모였으니 세금 높여서 더 최대로 찾기
            else right=mid-1;   //국가예산보다 더 모았으니 세금 줄이기
        }
        System.out.println(right);
    }
}
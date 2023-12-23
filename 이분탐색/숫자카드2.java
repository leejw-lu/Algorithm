package 이분탐색;
import java.io.*;
import java.util.*;
//10816번 숫자 카드2
public class 숫자카드2 {
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb= new StringBuilder();

        int n= Integer.parseInt(br.readLine());
        int[] arr= new int[n]; //현재 가지고 있는
        StringTokenizer st= new StringTokenizer(br.readLine());
        for (int i=0;i<n;i++)
            arr[i]=Integer.parseInt(st.nextToken());
        Arrays.sort(arr);

        int m= Integer.parseInt(br.readLine());
        st= new StringTokenizer(br.readLine());
        for (int i=0;i<m;i++){
            int key= Integer.parseInt(st.nextToken());
            sb.append(upperBound(arr,key)- lowerBound(arr,key)).append(' ');
        }
        System.out.println(sb);
    }

    private static int lowerBound(int[] arr, int key) {
        int left=0;
        int right=arr.length;

        while(left<right){
            int mid=(left+right)/2;
            if (key<=arr[mid]) right=mid;
            else left=mid+1;
        }
        return left;
    }

    private static int upperBound(int[] arr, int key) {
        int left=0;
        int right=arr.length;

        while(left<right){
            int mid=(left+right)/2;
            if (key<arr[mid]) right=mid;
            else left=mid+1;
        }
        return left;
    }
    
}

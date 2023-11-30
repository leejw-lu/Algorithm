import java.io.*;
import java.util.*;

//백준 15657번 N과 M(8) -> 중복조합
public class N과_M_8 {
    static int[] nums;
    static int[] arr;
    static int n, m;
    static StringBuilder sb= new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        n= Integer.parseInt(st.nextToken());
        m= Integer.parseInt(st.nextToken());
        nums= new int[n];
        arr= new int[n];

        st= new StringTokenizer(br.readLine());
        for (int i=0;i<n;i++)
            nums[i]=Integer.parseInt(st.nextToken());
        Arrays.sort(nums);
        dfs(0, 0);
        System.out.println(sb);

    }

    private static void dfs(int start, int depth) {
        if (depth==m) {
            for (int i=0;i<m;i++){
                sb.append(arr[i]).append(" ");
            }
            sb.append("\n");
            return;
        }
        for (int i=start;i<n;i++){
            arr[depth]=nums[i];
            dfs(i, depth+1);
        }
    }
}

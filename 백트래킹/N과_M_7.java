import java.io.*;
import java.util.*;

//백준 15656번 N과 M(7) -> 중복순열이라 visited 배열 필요X
public class N과_M_7 {
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
        dfs(0);
        System.out.println(sb);

    }

    private static void dfs(int depth) {
        if (depth==m) {
            for (int i=0;i<m;i++){
                sb.append(arr[i]).append(" ");
            }
            sb.append("\n");
            return;
        }
        for (int i=0;i<n;i++){
            arr[depth]=nums[i]; //depth=0,1 i=0 {nums[i]=1} //depth=0,1 i=1 {nums[1]=7}// depth=0,1 i=2 {nums[2]=8}
            dfs(depth+1);
        }
        
    }
}

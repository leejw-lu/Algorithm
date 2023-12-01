package 탐색;
import java.io.*;
import java.util.*;
//백준 13023번 ABCDE
public class ABCDE {
    static int n,m;
    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static int result=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());

        graph= new ArrayList[n];
        for (int i=0;i<n;i++) graph[i]= new ArrayList<>();
        visited= new boolean[n];
        
        for (int i=0;i<m;i++){
            st= new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            graph[a].add(b);
            graph[b].add(a);
        }

        for (int i=0;i<n;i++){
            visited[i] = true;
            dfs(i,0);
            if(result==1) break;    //친구관계 존재
            visited[i] = false;
        }

        System.out.println(result);
        
    }
    static void dfs(int idx, int depth) {
        if (depth>=4) {
            result=1;
            return;
        }
        //백트래킹
        for (int next : graph[idx]){
            if (!visited[next]){
                visited[next]=true;
                dfs(next, depth+1);
                visited[next]=false;
            }
        }
    }
    
}

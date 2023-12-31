import java.io.*;
import java.util.*;

//14889번 스타트와 링크
public class 스타트와_링크 {
    static int n;
    static int[][] graph;
    static boolean[] visited;
    static int min=Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        n= Integer.parseInt(br.readLine());
        graph=new int[n][n];
        visited=new boolean[n];

        for (int i=0;i<n;i++){
            StringTokenizer st= new StringTokenizer(br.readLine());
            for (int j=0;j<n;j++){
                graph[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        dfs(0,0);
        System.out.println(min);
    }

    private static void dfs(int idx, int count) {
        if (count==n/2){
            compareTeam(); //차이 검사
            return;
        }
        for (int i=idx;i<n;i++){
            if (!visited[i]){
                visited[i]=true;
                dfs(i+1,count+1);
                visited[i]=false;
            }
        }
    }

    private static void compareTeam() {
        int startTeam=0;
        int linkTeam=0;

        for (int i=0;i<n-1;i++){
            for (int j=i+1;j<n;j++){
                //모두 방문O 팀이면 startTeam
                if (visited[i] && visited[j]){ 
                    startTeam+=graph[i][j];
                     startTeam+=graph[j][i];
                }
                //모두 방문X 팀이면 linkTeam
                else if (!visited[i] && !visited[j]){ 
                    linkTeam+=graph[i][j];
                    linkTeam+=graph[j][i];
                }
            }
        }

        int diff=Math.abs(startTeam-linkTeam);
        if (diff==0){
            System.out.println(diff);
            System.exit(0);
        }

        min=Math.min(min,diff);
    }
}

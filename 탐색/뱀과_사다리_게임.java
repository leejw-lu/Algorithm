package 탐색;
import java.io.*;
import java.util.*;

//16928번 뱀과 사다리 게임
public class 뱀과_사다리_게임 {
    static int n,m;
    static int [] graph= new int[101];
    static int[] visited= new int[101];

    public static void main(String args[]) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());

        for (int i=1;i<=100;i++) graph[i]=i;
        Arrays.fill(visited,-1);

        //사다리, 뱀 정보 기록
        for (int i=0;i<n+m;i++){
            st=new StringTokenizer(br.readLine());
            int x=Integer.parseInt(st.nextToken());
            int y=Integer.parseInt(st.nextToken());
            graph[x]=y;
        }
        
        bfs(1);
        System.out.println(visited[100]);
    }

    static void bfs(int start) {
        Queue<Integer> q=new LinkedList<>();
        q.add(start);
        visited[start]=0;

        while(!q.isEmpty()){
            int cur=q.poll();
            for (int i=1;i<7;i++){  //주사위 1~6
                int next=cur+i;     //다음 도착지
                if (next>100) continue;
                next=graph[next]; //다음 도착지가 가리키는 위치로
                if (visited[next]==-1){     //아직 방문 안했으면 
                    visited[next]=visited[cur]+1;
                    q.add(next);
                }
            }    
        }
    }
}
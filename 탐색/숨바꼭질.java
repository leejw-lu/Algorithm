package 탐색;

import java.io.*;
import java.util.*;
//1697번 숨바꼭질
public class 숨바꼭질 {
    static int n, k;
    static int[] visited= new int[100001];
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        n=Integer.parseInt(st.nextToken());
        k=Integer.parseInt(st.nextToken());
        
        System.out.println(bfs(n));
    }

    static int bfs(int start){
        Queue<Integer> q= new LinkedList<>();
        q.add(start);

        while(!q.isEmpty()){
            int now=q.poll();

            if (now==k){
                return visited[now];
            }

            //x-1
            if (now-1>=0 && visited[now-1]==0){
                visited[now-1]=visited[now]+1;
                q.add(now-1);
            }
            //x+1
            if (now+1<=100000 && visited[now+1]==0){
                visited[now+1]=visited[now]+1;
                q.add(now+1);
            }
            //x*2
            if (now*2<=100000 && visited[now*2]==0){
                visited[now*2]=visited[now]+1;
                q.add(now*2);
            }
        }
        return -1;
    }
}

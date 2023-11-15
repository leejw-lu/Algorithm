package 탐색;
import java.util.*;
import java.io.*;

class Main {
    static int n,m;
    static int[][] graph;
    static int[][] virusGraph;
    static int dx[]={-1,1,0,0};
    static int dy[]={0,0,-1,1};
    static int result=Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());
        graph= new int[n][m];

        //입력
        for (int i=0;i<n;i++){
            st= new StringTokenizer(br.readLine());
            for (int j=0;j<m;j++){
                graph[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        makeWall(0);
        System.out.println(result);
    }

    //벽 3개 세우기 (완전탐색=백트래킹)
    static void makeWall(int wall){
        if (wall==3){
            bfs();
            return;
        }
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                if (graph[i][j]==0){
                    graph[i][j]=1; //벽 세우기
                    makeWall(wall+1);
                    graph[i][j]=0;
                }
    }

    //바이러스 퍼트리기
    static void bfs(){
        Queue<int[]> q=new LinkedList<>();
        virusGraph= new int[n][m];

        //1. 바이러스 찾아서 큐에 넣기
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++){
                virusGraph[i][j]=graph[i][j]; //wall이 3개 될때마다 실행해야하므로 초기화 용도
                if (virusGraph[i][j]==2)
                    q.add(new int[] {i,j});
            }

        //2. 바이러스 확산 하기
        while (!q.isEmpty()){
            int[] tmp=q.poll();
            int x=tmp[0];
            int y=tmp[1];

            for (int i=0;i<4;i++){
                int nx=x+dx[i];
                int ny=y+dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (virusGraph[nx][ny]==0){
                        virusGraph[nx][ny]=2;
                        q.add(new int[] {nx,ny});
                    }
                }
            }
        }

        //3. 안정 영역 크기 구하기
        int count=0;
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                if (virusGraph[i][j]==0)
                    count++;
        result=Math.max(result,count);
    }  

}

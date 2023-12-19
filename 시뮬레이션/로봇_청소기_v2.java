package 시뮬레이션;
import java.io.*;
import java.util.*;
//14503 로봇 청소기 (간단한 다른 풀이 version2)
public class 로봇_청소기_v2 {
    static int n,m;
    static int[][] graph;
    static int r,c,d;   //로봇 정보
	static int dx[] = {-1,0,1,0};  // 북동남서
	static int dy[] = {0,1,0,-1};
    static int result=1;

    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        n= Integer.parseInt(st.nextToken());
        m= Integer.parseInt(st.nextToken());
        graph=new int[n][m];

        st= new StringTokenizer(br.readLine());
        r=Integer.parseInt(st.nextToken());
        c=Integer.parseInt(st.nextToken());
        d=Integer.parseInt(st.nextToken());

        for (int i=0;i<n;i++){
            st= new StringTokenizer(br.readLine());
            for (int j=0;j<m;j++)
                graph[i][j]=Integer.parseInt(st.nextToken());
        }

        dfs(r,c,d);
        System.out.println(result);
    }

    static void dfs(int r, int c, int d) {
        graph[r][c]=-1;  //청소하기

        for (int i=0;i<4;i++){
            d= (d+3) % 4;   //반시계 90도 (왼쪽 방향으로 이동)
            int nx=r+dx[d];
            int ny=c+dy[d];

            //벽이 아니고 청소 안한 방 있는 경우
            if (nx>=0 && nx<n && ny>=0 && ny<m && graph[nx][ny]==0) { 
                result++;
                dfs(nx,ny,d);

                return; //return 안하면 후진해서 다른 곳 청소할 수 있음
            }
        }

        //이미 청소 & 벽인 경우
        int back= (d+2) % 4;
        int bx= r+ dx[back];
        int by= c+ dy[back];

        if (bx>=0 && bx<n && by>=0 && by<m && graph[bx][by] !=1)
            dfs(bx,by,d);
    }

}
package 탐색;
import java.io.*;
import java.util.*;
//2583번 영역 구하기
public class 영역_구하기 {
    static int n,m,k;
    static int[][] graph;
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};
    static int count=0;
    static ArrayList<Integer> countList=new ArrayList<>();

    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());
        k=Integer.parseInt(st.nextToken());

        graph=new int[n][m];    //0으로 초기화

        for (int i=0;i<k;i++){
            st=new StringTokenizer(br.readLine());
            int s_x=Integer.parseInt(st.nextToken());
            int s_y=Integer.parseInt(st.nextToken());
            int d_x=Integer.parseInt(st.nextToken());
            int d_y=Integer.parseInt(st.nextToken());

            makeRectangle(s_x,s_y,d_x,d_y);
        }

        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                if (graph[i][j]==0){    //빈 공간만 탐색하도록
                    count=0;
                    dfs(i,j);
                    countList.add(count);
                }
            }
        }

        System.out.println(countList.size());
        Collections.sort(countList);
        for (int i=0;i<countList.size();i++)
            System.out.print(countList.get(i)+" ");
    }

    static void makeRectangle(int s_x, int s_y, int d_x, int d_y) {
        for (int j=s_y;j<d_y;j++)
            for (int i=s_x;i<d_x;i++)
                graph[j][i]=-1;
    }

    static void dfs(int x, int y) {
        count++;
        graph[x][y]=-1; //방문

        for (int i=0;i<4;i++){
            int nx=x+dx[i];
            int ny=y+dy[i];
            if (nx>=0 && nx<n && ny>=0 && ny<m){
                if (graph[nx][ny]==0)
                    dfs(nx,ny);
            }
        }
    }

}

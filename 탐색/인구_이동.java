package 탐색;
import java.io.*;
import java.util.*;
//16234번 인구 이동
public class 인구_이동 {
    static int n,l,r;
    static int[][] graph;
    static ArrayList<int[]> union;
    static boolean[][] visited;
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};

    public static void main(String args[]) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        n=Integer.parseInt(st.nextToken());
        l=Integer.parseInt(st.nextToken());
        r=Integer.parseInt(st.nextToken());
        graph=new int[n][n];

        for (int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            for (int j=0;j<n;j++){
                graph[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(moveDay());
    }

    //인구 이동 day 구하기
    static int moveDay() {
        int day=0;
        while (true) {
            visited=new boolean[n][n];
            boolean isMove=false;

            for (int i=0;i<n;i++){
                for (int j=0;j<n;j++){
                    if (!visited[i][j]){
                        int sum=bfs(i,j);
                        if (union.size()>1){
                            changePopulation(sum);
                            isMove=true;    
                        }
                    }
                }
            }

            if(!isMove) 
                return day;
            day++;
        }
    }

    //인구 이동 후 인구 수
    static void changePopulation(int sum) {
        int avg=sum/union.size();
        for (int i=0;i<union.size();i++){
            int x=union.get(i)[0];
            int y=union.get(i)[1];
            graph[x][y]=avg;
        }
    }

    //bfs 돌며 연합 인구 수 합 reutrn
    static int bfs(int x, int y){
        Queue<int[]> q= new LinkedList<>();
        union= new ArrayList<>();

        visited[x][y]=true;
        q.add(new int[] {x,y});
        union.add(new int[] {x,y});
        int sum=graph[x][y];
		
		while(!q.isEmpty()) {
            int[] t=q.poll();

            for (int i=0;i<4;i++){
                int nx=t[0]+dx[i];
                int ny=t[1]+dy[i];
                if (nx>=0 && nx<n && ny>=0 && ny<n){
                    if (!visited[nx][ny]){
                        int dif=Math.abs(graph[t[0]][t[1]]-graph[nx][ny]);
                        if (dif>=l && dif<=r){
                            visited[nx][ny]=true;
                            q.add(new int[] {nx,ny});
                            union.add(new int[] {nx,ny});
                            sum+= graph[nx][ny];
                        }
                    }
                }
            }
        }
        return sum;
    }

}

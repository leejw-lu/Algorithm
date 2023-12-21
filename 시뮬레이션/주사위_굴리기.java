package 시뮬레이션;
import java.io.*;
import java.util.*;
//14499번 주사위 굴리기
public class 주사위_굴리기 {
    static int n,m;
    static int x,y,k;
    static int[][] graph;
    static int[] dy={1,-1,0,0}; //동서북남 방향 (x,y,n,m 방향 주의!!)
    static int[] dx={0,0,-1,1};
    static int[] dice=new int[7];   //주사위 배열 (1번 index가 윗면)

    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        n= Integer.parseInt(st.nextToken());
        m= Integer.parseInt(st.nextToken());
        x= Integer.parseInt(st.nextToken());
        y= Integer.parseInt(st.nextToken());
        k= Integer.parseInt(st.nextToken());

        graph=new int[n][m];

        for (int i=0;i<n;i++){
            st= new StringTokenizer(br.readLine());
            for (int j=0;j<m;j++)
                graph[i][j]= Integer.parseInt(st.nextToken());
        }

        st= new StringTokenizer(br.readLine());
        for (int i=0;i<k;i++){
            int cmd= Integer.parseInt(st.nextToken());
            move(cmd);
        }

    }

    private static void move(int cmd) {
        int nx=x+dx[cmd-1];
        int ny=y+dy[cmd-1];

        if (nx<0 || nx>=n || ny<0 || ny>=m) return;

        //주사위 이동
        int tmp=dice[1];
        switch (cmd) {
            case 1: //동
                dice[1]=dice[4];
                dice[4]=dice[6];
                dice[6]=dice[3];
                dice[3]=tmp;
                break;

            case 2: //서
                dice[1]=dice[3];
                dice[3]=dice[6];
                dice[6]=dice[4];
                dice[4]=tmp;
                break;

            case 3: //북
                dice[1]=dice[5];
                dice[5]=dice[6];
                dice[6]=dice[2];                    
                dice[2]=tmp;
                break;

            case 4: //남
                dice[1]=dice[2];
                dice[2]=dice[6];
                dice[6]=dice[5];
                dice[5]=tmp;
                break;
        }

        if (graph[nx][ny]==0){
            graph[nx][ny]=dice[6];
        }else{
            dice[6]=graph[nx][ny];
            graph[nx][ny]=0;
        }
        //x,y 이동
        x=nx; 
        y=ny;
        System.out.println(dice[1]); //윗면 출력
    }
}

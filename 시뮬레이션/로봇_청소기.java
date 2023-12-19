package 시뮬레이션;
import java.io.*;
import java.util.*;
//14503 로봇 청소기 (My 풀이 version1)
public class 로봇_청소기 {
    static int n,m;
    static int[][] graph;
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};
    static boolean notWall=true;
    static int result=0;
    //static Robot robot;

    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        /* 1. 입력 */
        n= Integer.parseInt(st.nextToken());
        m= Integer.parseInt(st.nextToken());
        graph=new int[n][m];

        Robot robot=new Robot();
        st= new StringTokenizer(br.readLine());
        robot.r=Integer.parseInt(st.nextToken());
        robot.c=Integer.parseInt(st.nextToken());
        robot.d=Integer.parseInt(st.nextToken());

        for (int i=0;i<n;i++){
            st= new StringTokenizer(br.readLine());
            for (int j=0;j<m;j++)
                graph[i][j]=Integer.parseInt(st.nextToken());
        }

        /* 2. 로봇 작동 */
        while(notWall){
            int x= robot.r;
            int y= robot.c;
            //Step1
            if (graph[x][y]==0) {
                graph[x][y]=2;  //청소
                result++;
            }
           
            //주변 4칸 조사
            int dirtyRoom=0;
            for (int i=0;i<4;i++){
                int nx=x+dx[i];
                int ny=y+dy[i];
                //벽이 아니고 청소안한 방 있는 경우
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (graph[nx][ny]==0) dirtyRoom+=1;
                }
            }

            //Step3
            if (dirtyRoom>0){
                //반시계 90도 회전
                if (robot.d==0) robot.d=3;
                else robot.d-=1;
                moveRobotFront(robot);
            } //Step2
            else{ 
                checkRobotBack(robot);
            }        
        }

        /*3. 출력 */
        System.out.println(result);
    }

    //바라보는 방향으로 한칸 전진
    private static void moveRobotFront(Robot robot) {
        int d=robot.d;
        int tx=robot.r;
        int ty=robot.c;

        if (d==0) tx=tx-1;    //북
        else if (d==1) ty=ty+1;   //동
        else if (d==2) tx=tx+1;   //남
        else ty=ty-1;       //서

        //전진 했을 때 청소 여부 확인 (graph==0) &  로봇 한칸 전진
        if (tx >= 0 && tx < n && ty >= 0 && ty < m) {
            if (graph[tx][ty]==0){
                robot.r=tx;
                robot.c=ty;
            }
        }
    }

    //한칸 후진 후 벽인지 체크
    private static void checkRobotBack(Robot robot) {
        int d=robot.d;
        int tx=robot.r;
        int ty=robot.c;

        if (d==0) tx=tx+1;    //북
        else if (d==1) ty=ty-1;   //동
        else if (d==2) tx=tx-1;   //남
        else ty=ty+1;         //서

        //후진했을 때 벽 체크
        if (tx >= 0 && tx < n && ty >= 0 && ty < m) {
            if (graph[tx][ty]==1) notWall=false;
            else {
                //후진
                robot.r=tx;
                robot.c=ty;
            }
        }
    }
   
}

class Robot{
    int r;  //(r,c)
    int c;  
    int d;  //바라보는 방향
}
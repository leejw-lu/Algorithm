package 탐색;
import java.util.*;
import java.io.*;

//2667번 단지번호 붙이기
class Main {
    final static int MAX=25+10;
    static boolean[][] graph;
    static int countPerDanji;
    static int dirX[]={-1,1,0,0};
    static int dirY[]={0,0,-1,1};

    static void dfs(int x, int y){
        graph[x][y]=false;
        countPerDanji++;

        for(int i=0;i<4;i++){
            int newX=x+dirX[i];
            int newY=y+dirY[i];
            if(graph[newX][newY])
                dfs(newX,newY);
        }
    }
    
    public static void main(String[] arsgs) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());

        graph=new boolean[MAX][MAX];

        //1. 그래프 정보 입력
        for (int i=1;i<=N;i++){
            String s=br.readLine();
            for (int j=1; j<=N; j++)
                graph[i][j]=s.charAt(j-1)=='1';
        }
        //2. dfs 수행
        ArrayList<Integer> countList=new ArrayList<>();
        for (int i=1;i<=N;i++)
            for (int j=1;j<=N;j++)
                if (graph[i][j]) {
                    countPerDanji=0;
                    dfs(i,j);
                    countList.add(countPerDanji);
                }
        //3.출력
        System.out.println(countList.size());
        Collections.sort(countList);
        for (int i=0;i<countList.size();i++)
            System.out.println(countList.get(i));
        br.close();
    }
}

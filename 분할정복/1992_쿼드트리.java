package 분할정복;
import java.util.*;
import java.io.*;

public class B1992 {

    static int[][] graph;
    static StringBuilder sb=new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());
        graph= new int[N][N];
        StringTokenizer st;

        for(int i=0;i<N;i++){
            String s=br.readLine();
            for(int j=0;j<N;j++)
                graph[i][j]=s.charAt(j)-'0';
        }

        quadTree(0,0,N);
        System.out.println(sb);
    }

    public static void quadTree(int row, int col, int size) {
        //색상 비교
        if(colorCheck(row,col,size)) {
            sb.append(graph[row][col]); 
        }
        else{   //색 다르면 분할
            int newSize=size/2; //절반 사이즈

            sb.append('(');

            quadTree(row, col, newSize);           //왼쪽 위
            quadTree(row, col+newSize, newSize);   //오른쪽 위
            quadTree(row + newSize, col, newSize); //왼쪽 아래
            quadTree(row + newSize, col+newSize, newSize); //오른쪽 아래
            
            sb.append(')');
        }
    }

    public static boolean colorCheck(int x, int y, int size){
        int color=graph[x][y];

        for (int i=x;i<x+size;i++){
            for (int j=y;j<y+size;j++){
                if (graph[i][j] != color)
                    return false;
            }
        }
        return true;
    }

}
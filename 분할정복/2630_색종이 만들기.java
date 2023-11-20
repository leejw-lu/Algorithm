package 분할정복;
import java.util.*;
import java.io.*;

public class Main { 
    static int[][] graph;
    static int white=0;
    static int blue=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());
       
        graph= new int[N][N];
        StringTokenizer st;

		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j < N; j++) 
				graph[i][j] = Integer.parseInt(st.nextToken());
		}

        partition(0,0,N);

        System.out.println(white);
        System.out.println(blue);

    }

    public static void partition(int row, int col, int size) {
        //색상 비교
        if(colorCheck(row,col,size)) {
            if(graph[row][col]==0)
                white++;
            else
                blue++;
            return;
        }

        int newSize=size/2; //절반 사이즈

		partition(row, col, newSize);						// 2사분면
		partition(row, col + newSize, newSize);				// 1사분면
		partition(row + newSize, col, newSize);				// 3사분면
		partition(row + newSize, col + newSize, newSize);	// 4사분면
    }

    //한 사분면에 색상 모두 같은 지 비교 함수
    public static boolean colorCheck(int row, int col, int size){
        int color=graph[row][col];

        for (int i=row;i<row+size;i++){
            for (int j=col;j<col+size;j++){
                if (graph[i][j] != color)
                    return false;
            }
        }
        return true;
    }

}

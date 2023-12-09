package 구현;
import java.io.*;
import java.util.*;

//16935번 배열 돌리기3
public class 배열_돌리기3 {
    static int n,m,r;
    static int[][] graph;
    static int[][] ngraph;
    static int num;
    static StringBuilder sb= new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        
        //1. 입력
        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());
        r=Integer.parseInt(st.nextToken());
        graph= new int[n][m];

        for (int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            for (int j=0;j<m;j++) {
                graph[i][j]=Integer.parseInt(st.nextToken());
            }
        }
        
        //2. 배열 돌리기
        st= new StringTokenizer(br.readLine());
        for (int i=0;i<r;i++){
            num=Integer.parseInt(st.nextToken());

            switch (num) {
                case 1: //상하반전
                    upDown();
                    break;

                case 2: //좌우 반전
                    leftRight();
                    break;

                case 3: //오른쪽 90도 회전
                    rightRotation();
                    break;

                case 4: //왼쪽 90도 회전
                    lefttRotation();
                    break;

                case 5: //1->2, 2->3, 3->4, 4->1
                    five();
                    break;
                
                case 6: //1->4, 4->3, 3->2, 2->1
                    six();
                    break;
            }
        }

        //3. 출력
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++) 
                sb.append(graph[i][j]+" ");
            sb.append("\n");
        }
        System.out.println(sb);
    }

    //1. 상하반전
    private static void upDown() {
        ngraph= new int[n][m];
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                ngraph[i][j]=graph[n-i-1][j];
        graph=ngraph;
    }

    //2. 좌우반전
    private static void leftRight() {
        ngraph= new int[n][m];
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                ngraph[i][j]=graph[i][m-j-1];
        graph=ngraph;
    }

    //3. 오른쪽 90도
    private static void rightRotation() {
        ngraph= new int[m][n];  //배열 크기 바뀜
        for (int i=0;i<m;i++)
            for (int j=0;j<n;j++)
                ngraph[i][j]=graph[n-j-1][i];
        
        //배열 크기 바꾸기
        int tmp=n;
        n=m;
        m=tmp;
        graph=ngraph;
    }
    
    //4. 왼쪽 90도
    private static void lefttRotation() {
        ngraph= new int[m][n];  //배열크기 바뀜
        for (int i=0;i<m;i++)
            for (int j=0;j<n;j++)
                ngraph[i][j]=graph[j][m-i-1];

        //배열 크기 바꾸기
        int tmp=n;
        n=m;
        m=tmp;
        graph=ngraph;
    }

    //5. 
    private static void five() {
        ngraph= new int[n][m];
        for (int i=0;i<n/2;i++)
            for (int j=0;j<m/2;j++){
                ngraph[i][j] = graph[i][j];				// 1 백업
                graph[i][j] = graph[i + n/2][j];			// 4 -> 1
                graph[i + n/2][j] = graph[i + n/2][j + m/2];// 3 -> 4
                graph[i + n/2][j + m/2] = graph[i][j + m/2];// 2 -> 3
                graph[i][j + m/2] = ngraph[i][j];			// 1 -> 2
            }
    }

    //6.
    private static void six() {
        ngraph= new int[n][m];
        for (int i=0;i<n/2;i++)
            for (int j=0;j<m/2;j++){
                ngraph[i][j] = graph[i][j];				// 1 백업
                graph[i][j] = graph[i][j + m/2];			// 2 -> 1
                graph[i][j + m/2] = graph[i + n/2][j + m/2];// 3 -> 2
                graph[i + n/2][j + m/2] = graph[i + n/2][j];// 4 -> 3
                graph[i + n/2][j] = ngraph[i][j];			// 1 -> 4
            }
    }
}

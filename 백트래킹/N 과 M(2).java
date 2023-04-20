import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {  

    static int N,M;
    static int [] arr;  //주어진 숫자
    static boolean visited[];  //방문, 중복 금지
    static StringBuffer sb=new StringBuffer(); //출력

    public static void main(String[] args) throws IOException {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine()," ");

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        arr= new int[M];
        visited= new boolean[N];

        dfs(0);
        System.out.println(sb);
    }

    public static void dfs(int depth){
        //재귀 끝낼 조건
        if (depth==M){ // M=2이면 _ _ 2자리수.
            for (int x: arr){
                sb.append(x).append(' ');
            }
            sb.append('\n');
            return;
        }

        for (int i=0;i<N;i++){
            if(!visited[i]) {
                if(depth==0 || arr[depth-1]<i+1 ){
                    arr[depth]=i+1;         //현재 인덱스에 값 넣어주고
                    visited[i]=true;        //방문표시
                    dfs(depth+1);     //다음 인덱스 채우기 위해 다시 재귀호출
                    visited[i]=false;
                }

            }
        }

    }
}

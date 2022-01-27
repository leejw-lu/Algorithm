import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int N,M;
    static int [] arr;  
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
                arr[depth]=i+1;
                visited[i]=true;
                dfs(depth+1);         //dfs호출
                visited[i]=false;     //출력한담 return하고 false로바꿈. 그래야 다음i번째에서도 visited사용 가능.
            }
        }

    }
}

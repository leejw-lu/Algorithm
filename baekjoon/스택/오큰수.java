import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] arsgs) throws IOException{

        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> stack=new Stack<Integer>();

        int n=Integer.parseInt(br.readLine());
        int [] seq=new int[n];
        int [] ans=new int[n];

        StringTokenizer st=new StringTokenizer(br.readLine()," ");
        for(int i=0;i<n;i++){
            seq[i]=Integer.parseInt(st.nextToken());    //seq배열엔 입력한 숫자들 들어있음
            ans[i]=-1;  //ans -1로 초기화.
        }

        for(int i=0;i<n;i++){
            while(!stack.empty() && seq[stack.peek()]< seq[i] ){
                ans[stack.pop()]=seq[i];
            }
            stack.push(i);
        }

        StringBuilder sb=new StringBuilder();
        for(int v : ans){
            sb.append(v).append(' ');
        }

        System.out.println(sb);
    }
}

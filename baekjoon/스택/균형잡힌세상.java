import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] arsgs) throws IOException {

        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        String s;

        while(true){

            Stack<Character> st=new Stack<Character>();    //한줄읽을때마다 새로운스택

            s=br.readLine();

            if(s.equals(".")){
                break;
            }

            for(int i=0;i<s.length();i++){
               char temp=s.charAt(i);   //i번째 문자
                if (temp == '(' || temp == '[') {
                    st.push(temp);
                } else if (temp == ')' || temp == ']') {
                    if (st.empty() || (st.peek() == '(' && temp == ']') || (st.peek() == '[' && temp == ')')) {
                        st.push(temp);
                        break;
                    }
                    st.pop();
                }
            }

            if(st.empty()){
                sb.append("yes").append("\n");
            } else{
                sb.append("no").append("\n");
            }

        }

        System.out.println(sb);

    }
}

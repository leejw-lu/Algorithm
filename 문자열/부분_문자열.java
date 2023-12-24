package 문자열;
import java.io.*;
import java.util.*;
//6550번 부분 문자열
public class 부분_문자열 {
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String str, s, t;
        int idx;

        while (true) {
            str=br.readLine();
            if (str==null) break;

            st= new StringTokenizer(str);
            s= st.nextToken();
            t= st.nextToken();

            idx=0;  //초기화
            for (int i=0;i<t.length();i++){
                if (s.charAt(idx)==t.charAt(i)) idx++;
                if (idx==s.length()) break;
            }

            if (idx==s.length()) System.out.println("Yes");
            else System.out.println("No");
        }
        
    }
    
}

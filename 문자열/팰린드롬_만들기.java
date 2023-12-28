package 문자열;
import java.io.*;
//1254번 팰린드롬 만들기
public class 팰린드롬_만들기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        String s=br.readLine();
        int idx= s.length();
        for (int i=0;i<s.length();i++){
            if (isPalind(s.substring(i))) 
                break;
            idx++;
        }
        System.out.println(idx);
    }
    private static boolean isPalind(String s){
        int start=0;
        int last=s.length()-1;
        while (start<=last){
            if (s.charAt(start) != s.charAt(last))
                return false;
            start++;
            last--;
        }
        return true;
    }
}

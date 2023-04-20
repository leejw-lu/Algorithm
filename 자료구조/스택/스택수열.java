import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();    //+,-출력할 결과물 저장
        Stack<Integer> stack = new Stack<>();

        int N= Integer.parseInt(br.readLine()); //첫줄엔 N개 개수
        int start=0;

        while(N --> 0){
            int value=Integer.parseInt(br.readLine());

            if(value > start){
                for(int i= start+1; i<=value; i++){
                    stack.push(i);
                    sb.append("+").append("\n");
                }
                start=value;    //다음 push할때 오름차순 유지하기 위한 변수초기화.

            } else if(stack.peek() != value) { //맨위top 원소가 입력받은 value값과 같지 않은경우
                System.out.println("NO"); //바보다,,,,,No가 아니라 NO임......
                return;
            }
            stack.pop();
            sb.append("-").append("\n");
        }
        System.out.println(sb);
    }
}

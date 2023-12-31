package 그리디;
import java.io.*;
import java.util.*;

//1744번 수 묶기
public class 수_묶기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        int n= Integer.parseInt(br.readLine());

        PriorityQueue<Integer> plus= new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minus= new PriorityQueue<>();
        int one=0; //1은 곱하는 것보다 더하는 것이 최대
        int zero=0;
        int result=0;

        for (int i=0;i<n;i++){
            int num=Integer.parseInt(br.readLine());
            if (num==1) one++;      //num==1을 num>0보다 먼저하기!
            else if (num==0) zero++;
            else if (num>0) plus.add(num);
            else minus.add(num);
        }

        //양수는 내림차순 정렬대로 2개씩 곱한 뒤 
        //남은 1개가 있으면 더하기
        while (plus.size()>1) {
            int a= plus.poll();
            int b= plus.poll();
            result+= a*b;
        }
        if (!plus.isEmpty()) result+=plus.poll();

        //음수는 오름차순 대로 2개씩 곱한 뒤 (음*음=양 이므로)
        //남은 1개가 있으면 0있는지 확인 후 (음*0= 0) 없으면 남은 수(-) 더하기
        while (minus.size()>1){
            int a= minus.poll();
            int b= minus.poll();
            result+= a*b;
        }
        if (!minus.isEmpty() && zero==0) result+= minus.poll();

        //1의 개수 더하기
        result+=one;

        System.out.println(result);
    }
}

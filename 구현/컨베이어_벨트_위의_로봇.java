package 구현;
import java.io.*;
import java.util.*;
//20055번 컨베이어 벨트 위의 로봇
public class 컨베이어_벨트_위의_로봇 {
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());

        int n= Integer.parseInt(st.nextToken());
        int k= Integer.parseInt(st.nextToken());

        int size=2*n;
        int[] A=new int[size];
        boolean[] robots= new boolean[n];

        st= new StringTokenizer(br.readLine());
        for (int i=0;i<size;i++)
            A[i]=Integer.parseInt(st.nextToken());

        int level=0;

        while(true) {
            level++;

            //Step1: 벨트, 로봇 이동
            int tmp=A[size-1];
            for (int i=size-1;i>0;i--)
                A[i]=A[i-1];
            A[0]=tmp;

            for (int i=n-1;i>0;i--) 
                robots[i]=robots[i-1];
            robots[0]=false;    //1번 올리는 위치 무조건 빈다.
            robots[n-1]=false;  //N번 내리는 위치 무조건 빈다.

            //Stpe2. 로봇 이동
            for (int i=n-1;i>0;i--){
                if (robots[i-1] && !robots[i] && A[i]>=1){   //현재칸 로봇O, 이동하려는 칸에 로봇X, 그 칸의 내구도가 1 이상
                    robots[i]=true;     //다음칸으로 이동
                    robots[i-1]=false;  //현재칸 비움
                    A[i]--;             //내구성 -
                }
            }

            //Step3. 로봇 올리기
            if (A[0]!=0) {
                robots[0]=true;
                A[0]--;
            }

            //Step4. 내구도가 0인 칸의 개수가 K개 이상이라면 종료
            int count=0;
            for (int i=0;i<size;i++)
                if (A[i]==0) count++;
            if (count>=k) break;
        }

        System.out.println(level);
    }
}

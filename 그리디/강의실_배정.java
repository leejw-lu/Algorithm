package 그리디;
import java.io.*;
import java.util.*;
//11000번 강의실 배정
public class 강의실_배정 {
    static int n;
    static int[][] arr;
    static PriorityQueue<Integer> pq= new PriorityQueue<>();

    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n=Integer.parseInt(br.readLine());
        arr=new int[n][2];

        for (int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            arr[i][0]=Integer.parseInt(st.nextToken());
            arr[i][1]=Integer.parseInt(st.nextToken());
        }

        //시작시간[0] 기준 정렬, 같으면 끝나는시간[1] 정렬
        Arrays.sort(arr, new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2){
                if (o1[0]==o2[0]) return o1[1]-o2[1];
                return o1[0]-o2[0];
            }
        });

        pq.add(arr[0][1]);

        for (int i=1;i<n;i++){
            if (pq.peek()<=arr[i][0]) //시작시간이 끝나는 시간보다 느리거나 같은 경우
                pq.poll();
            pq.add(arr[i][1]);
        }
        System.out.println(pq.size());
    }
}

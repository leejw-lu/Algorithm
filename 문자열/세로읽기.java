package 문자열;

import java.io.*;
//10798번 세로읽기
public class 세로읽기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb= new StringBuilder();

        char[][] arr= new char[5][15];

        //입력
        for (int i=0;i<5;i++){
            String str= br.readLine();
            for (int j=0;j<str.length();j++)
                arr[i][j]=str.charAt(j);
        }

        //출력
        for (int j=0;j<arr[0].length;j++){  //가로 최대 15개
            for (int i=0;i<5;i++){          //총 5줄
                if (arr[i][j]=='\0') continue;
                sb.append(arr[i][j]);
            }
        }
        System.out.println(sb);
    }
}

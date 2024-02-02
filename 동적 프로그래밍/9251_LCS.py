#LCS: 최장 공통 부분 문자열 (연속적이지 X)
import sys
read=sys.stdin.readline
s1=read().rstrip() #ACAYKP
s2=read().rstrip() #CAPCAK

dp=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1]==s2[j-1]:       #서로 추가된 문자가 같은 경우
            dp[i][j]=dp[i-1][j-1]+1 
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1][-1])

import sys
read=sys.stdin.readline

T=int(read())
for _ in range(T):
    N,M=map(int,read().split())
    dp=[[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,M+1):
            if i==1:
                dp[i][j]=j
                continue
            if i==j:
                dp[i][j]=1
            else:
                if j>i:
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
    print(dp[N][M])

#조합으로도 풀 수 O 이 문제는 DP로 연습.
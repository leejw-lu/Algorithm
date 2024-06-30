def solution(m, n, puddles):
    answer = 0
    dp=[[0]*m for _ in range(n)] #학교까지 최단거리 수
    dp[0][0]=1
    
    for (y,x) in puddles:
        dp[x-1][y-1]=-1
    
    for i in range(n):
        for j in range(m):
            if dp[i][j]!=-1:
                
                #오른쪽 
                if j+1<m and dp[i][j+1]!=-1: 
                    dp[i][j+1]+=dp[i][j]

                #아래쪽
                if i+1<n and dp[i+1][j]!=-1:
                    dp[i+1][j]+=dp[i][j]

    return dp[-1][-1] %1000000007
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)] #(0,0) -> (m-1,n-1)까지 가는 경우의 수
        dp[0][0]=1 #초기화 해야함.

        for i in range(m):
            for j in range(n):
                #bottom
                if i + 1 <m:
                    dp[i+1][j]+=dp[i][j]
                #right
                if j + 1 <n:
                    dp[i][j+1]+=dp[i][j]
        return dp[-1][-1]
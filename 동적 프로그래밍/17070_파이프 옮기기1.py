n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

dp=[[[0]*3 for _ in range(n)] for _ in range(n)] #파이프 끝의 개수
#dp[x][y][dir]
dp[0][1][0]=1 #초기위치 (dir=가로)

#1행은 가로만. 1열은 애초에 파이프 X
for i in range(2,n):
    if graph[0][i]==0:
        dp[0][i][0]=dp[0][i-1][0]

for i in range(1,n):
    for j in range(1,n):
        if graph[i][j]: #벽 있으면 pass
            continue

        #가로 이동 : (이전 위치의) 가로+대각선
        dp[i][j][0]=dp[i][j-1][0]+dp[i][j-1][2]

        #세로 이동 : 세로+대각선
        dp[i][j][1]=dp[i-1][j][1]+dp[i-1][j][2]

        #대각선 이동 : 가로+세로+대각선
        if graph[i-1][j]==0 and graph[i][j-1]==0:
            dp[i][j][2]=dp[i-1][j-1][0]+dp[i-1][j-1][1]+dp[i-1][j-1][2]

print(sum(dp[n-1][n-1]))
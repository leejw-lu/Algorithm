import sys
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)] #(0,0)->(n-1,n-1)까지 가는 경우의 수 담기
dp[0][0]=1

for i in range(n):
    for j in range(n):
        step=graph[i][j]

        if step==0 or dp[i][j]==0:
            continue

        #오른쪽
        if j+step<n:
            dp[i][j+step]+=dp[i][j]
        #아래쪽
        if i+step<n:
            dp[i+step][j]+=dp[i][j]

print(dp[-1][-1])

#bfs로 q.append 했는데 그럼 메모리 초과 나온다.
#그래프가 보인다고 바로 BFS, DFS 하는 것이 아님.

import sys
read=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,sum,depth):
    global result
    if result >= sum + maxValue*(3-depth): #탐색을 계속 진행해도 최댓값 X
        return
    if depth==3: #총 블록 4개 활용
        result=max(result, sum)
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m: 
            continue
        if not visited[nx][ny]:
            if depth==1: #ㅜ 모양 (다음노드가 아닌 이전노드에서 dfs)
                visited[nx][ny]=True
                dfs(x,y, sum+graph[nx][ny], depth+1)
                visited[nx][ny]=False
            #ㅡ, ㅁ, L , Z 모양 -> 다음노드 dfs
            visited[nx][ny]=True
            dfs(nx,ny, sum+graph[nx][ny], depth+1)
            visited[nx][ny]=False
            
#입력
n,m=map(int,read().split())
graph=[list(map(int,read().split())) for _ in range(n)]
visited=[[False]*(m) for _ in range(n)]

result=0    #최댓값
maxValue=max(map(max, graph)) #graph중 최댓값

for i in range(n):
    for j in range(m):
        visited[i][j]=True
        dfs(i,j, graph[i][j], 0)
        visited[i][j]=False

print(result)
from collections import deque
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
move=[list(map(int,input().split())) for _ in range(m)] # d s

cloud=deque([(n-2,0),(n-2,1),(n-1,0), (n-1,1)]) #구름 초기 위치
direct=[[0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1]]

for _ in range(m): #m번 이동
    #1. 구름 이동 & 2. 비 내리기
    d,s= move[_]
    waterPlus=[]
    visited=[[False]*n for _ in range(n)] #visited안쓰고 waterPlus에 (i,j) in 있는지 확인하면 시간초과 발생

    while cloud:
        x,y=cloud.popleft()
        nx,ny=(x + s*direct[d-1][0]) %n, (y + s*direct[d-1][1]) %n
        waterPlus.append((nx,ny))
        visited[nx][ny]=True
        graph[nx][ny]+=1

    #3. 물 증가한 칸에 마법 시전
    for w in range(len(waterPlus)):
        x, y = waterPlus[w][0], waterPlus[w][1]
        count=0
        for k in range(1,8,2): #대각선 방향: d의 1,3,5,7번 idx
            nx,ny= x+direct[k][0], y+direct[k][1]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny]>0: count+=1
        graph[x][y]+=count

    #4. 구름 있던 곳 제외 물의 양 2이상인 곳 구름 생성 -> 물의양 2 minus
    for i in range(n):
        for j in range(n):
            # if (i, j) not in waterPlus:  # 구름 있던 곳 제외 >>> in 쓰면 시간초과 난다!!
            if graph[i][j]>=2 and not visited[i][j]: #구름 있던 곳 제외 구름 생성
                cloud.append((i,j))
                graph[i][j]-=2

result=0
for g in graph:
    result+=sum(g)
print(result)
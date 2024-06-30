from collections import deque
n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

#상어 초기 위치 찾기
shark_x, shark_y, size=0,0,2 #(x,y,상어크기)
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            shark_x, shark_y=i,j
            graph[i][j]=0

#물고기 찾기
def findFish(sx,sy):
    global size
    distance=[[0]*n for _ in range(n)]
    visited=[[False]*n for _ in range(n)]
    visited[sx][sy]=True
    
    fishList=[]

    q=deque()
    q.append((sx,sy))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny] and graph[nx][ny]<=size: #상어 이동 가능
                visited[nx][ny]=True
                distance[nx][ny]=distance[x][y]+1
                q.append((nx,ny)) #상어 이동

                #물고기 존재 & 먹을 수 있다면 담기
                if graph[nx][ny]<size and graph[nx][ny] !=0: 
                    fishList.append((nx,ny,distance[nx][ny])) #물고기 좌표, 거리

    fishList.sort(key=lambda x: (x[2],x[0],x[1])) #거리가까운, x(가장 위), y(가장 왼쪽) 순으로.
    return fishList
    #return sorted(fishList, key=lambda x: (-x[2], -x[0], -x[1])) >> fishList.pop() 하면 정렬 뒤에꺼가 나와서 - 붙여야함. #56행 주석 참고.

result=0
eatCount=0
#맨 앞 후보만 먹고 다시 bfs 해야함.-> 상어 이동 후 거리 달라져서 우선순위 달라짐.
while True:
    fishList=findFish(shark_x,shark_y) # fishList:  [(0, 3, 3), (3, 0, 3)]

    if len(fishList)==0: #더이상 먹을 물고기 X-> 엄마상어에 요청=== 종료 조건.
        break
    
    nx,ny,time=fishList[0]  #popright() 대신 fishList[0] 사용. []는 pop만 가능. 그래서 .pop() 하면 (0,3,3)이 아닌 (3,0,3)이 나오므로 정렬을 -x[2],-x[0],x[1]해줘야함.
    #print("pop: ", nx, ny, time)

    result+=time #움직인 거리 수가 곧, 시간.
    graph[shark_x][shark_y],graph[nx][ny]=0,0

    #!!!!!상어좌표 옮기기!!!!!!
    shark_x,shark_y=nx,ny

    eatCount+=1
    if size==eatCount: #상어크기와 같은 수의 물고기 먹을때마다. ex)상어size2는 물고기 2마리를 먹어야 3이 된다.
        eatCount=0
        size+=1

print(result)
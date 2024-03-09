import copy
n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
cctv=[]

mode=[
    [],
    [[0],[1],[2],[3]], #cctv 1번
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    [[0,1,2,3]] ]

dx=[-1,0,1,0] #북동남서 (90도 회전)
dy=[0,1,0,-1]

#cctv 위치 append하기
for i in range(n):
    for j in range(m):
        if graph[i][j]!=0 and graph[i][j]!=6: #1~5번 cctv
            cctv.append((i,j,graph[i][j]))

def monitor(x,y,graph,mode):
    for i in mode:  #[0,1]
        nx=x #cctv위치는 고정적이므로. 감시하기 위해 여기에서 선언 해야함!!!!
        ny=y
        while True:
            nx,ny=nx+dx[i],ny+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                break
            if graph[nx][ny]==6: #벽이면
                break
            elif graph[nx][ny]==0:
                graph[nx][ny]=-1

def dfs(depth, graph):
    global blindSpot
    if depth==len(cctv):
        count=0
        for i in range(n):
            count+=graph[i].count(0)
        blindSpot=min(blindSpot,count)
        return
    
    temp=copy.deepcopy(graph)   #graph 복제
    x,y,num=cctv[depth]     #탐색할 cctv
    for i in mode[num]:     #[[0,1],[1,2],[2,3],[0,3]]
        monitor(x,y,temp,i)  
        dfs(depth+1,temp) 
        temp=copy.deepcopy(graph) #보드 초기화

blindSpot=int(1e9)
dfs(0,graph)
print(blindSpot)
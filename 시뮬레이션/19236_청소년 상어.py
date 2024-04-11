import copy

graph=[[] for _ in range(4)]
direct=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

#입력
for i in range(4):
    data=list(map(int,input().split()))
    fish=[]
    for j in range(4): #(번호,방향)
        fish.append([data[2*j], data[2*j+1]-1]) #방향-1하기
    graph[i]=fish

#상어 위치/방향 초기화
#sharkPos=[0,0]
result=0

def change_dir_or_switch(x,y,d,graph, sharkPos):
    nd=d
    change = True
    while change: #방향 이동할 수 있을 때 까지
        nx, ny = x + direct[nd][0], y + direct[nd][1]
        # 이동 불가-> 상어 or 공간 밖
        if (nx, ny) == sharkPos or nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            nd = (nd + 1) % 8
            continue

        #이동가능: switch
        change=False
        graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
        if d!=nd: #방향 바꾸기
            graph[nx][ny][1] = nd

def find_fish_pos(num, graph):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return i, j
    return -1, -1

#모든 물고기 이동 시키는 함수
def fish_move(graph, sharkPos):
    for start in range(16):
        #start 번호 착기
        i, j = find_fish_pos(start+1, graph) #i,j좌표 찾아야지 안그러면 계속 반복된다.
        if i!=-1 and j!=-1:
            d=graph[i][j][1]
            change_dir_or_switch(i,j,d,graph, sharkPos)
    #print("graph: ", graph)

def get_shark_movable(x,y,graph):
    d=graph[x][y][1]
    position=[]
    for _ in range(4):
        nx,ny=x+direct[d][0],y+direct[d][1]
        if 0<=nx<4 and 0<=ny<4 and graph[nx][ny][0]!=-1:
            position.append((nx,ny))
        x,y=nx,ny   #point1: 좌표 update 해야함!!!!
    return position

def dfs(graph,sharkPos,total):
    global result
    graph=copy.deepcopy(graph)
    x,y=sharkPos[0],sharkPos[1]

    #물고기 잡아먹기
    total+=graph[x][y][0]
    graph[x][y][0]=-1

    # 물고기 이동
    fish_move(graph, (x,y)) #graph, point2: 상어좌표!! (상어좌표 계속 update해야함.)

    # 상어 이동가능한 좌표 구하기
    position=get_shark_movable(x,y,graph)

    if len(position)==0:
        result=max(result,total)
        return
    for nx, ny in position:
        dfs(graph,(nx,ny),total)


#상어 이동
dfs(graph,(0,0),0)
print(result)
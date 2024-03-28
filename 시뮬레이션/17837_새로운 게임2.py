n,k=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
chess=[[[] for _ in range(n)] for _ in range(n)]
piece=[] #(x,y,d)

dx=[0,0,-1,1] #->, <-, up, down
dy=[1,-1,0,0]

for i in range(k):
    x,y,d=map(int,input().split())
    piece.append([x-1,y-1,d-1]) #체스xy좌표, 방향d
    chess[x-1][y-1].append(i)

def change_dir(d):
    if d==0: return 1
    elif d==1: return 0
    elif d==2: return 3
    else: return 2

def move(piece_num):
    x,y,d=piece[piece_num]
    nx,ny=x+dx[d], y+dy[d]
    
    #1) 범위 밖이거나 Blue
    if nx<0 or nx>=n or ny<0 or ny>=n or graph[nx][ny]==2: 
        nd=change_dir(d)
        piece[piece_num][2]=nd #피스 방향 바꾼 값 반영하기
        nx,ny=x+dx[nd], y+dy[nd]
        if nx<0 or nx>=n or ny<0 or ny>=n or graph[nx][ny]==2:
            return False
    
    pieceAdd=[]
    #말 이동시키기 (흰,빨 공통)
    for idx, number in enumerate(chess[x][y]):
        if number==piece_num:
            pieceAdd.extend(chess[x][y][idx:])
            chess[x][y]=chess[x][y][:idx] #num 위에만 옮기니까.
            break
    
    #빨간색
    if graph[nx][ny]==1: #피스 거꾸로
        #pieceAdd=pieceAdd[-1::-1]  >> 하,,,-1::-1인데 -1::1 써서 계속 틀렸음.
        pieceAdd.reverse() 

    for p in pieceAdd:
        piece[p][0],piece[p][1]=nx,ny #이동한 피스 정보 update
        chess[nx][ny].append(p) #피스 쌓아 올리기
    
    if len(chess[nx][ny]) >=4:
        return True
    return False

count=1
while count<=1000:
    for i in range(k):
        flag=move(i)
        if flag: #종료조건 True
            print(count)
            exit()
    count+=1
print(-1) #1000보다 크면 출력
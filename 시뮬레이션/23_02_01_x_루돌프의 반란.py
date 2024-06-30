from collections import deque
n,m,p,c,D=map(int,input().split())

rx,ry=map(int,input().split()) #루돌프 초기위치
rx-=1
ry-=1
graph=[[0]*n for _ in range(n)]
graph[rx][ry]=-1 #루돌프 현재 위치
score=[0]*(p+1) #산타 score
canSantaMove=[1]*(p+1) #1이면 산타 이동 가능/ 0이면 산타 튕겨져 나감
canSantaMove[0]=0
koSanta=[0]*(p+1) #기절/ 2면 기절 time -1씩 하기.

direct=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)] #루돌프 모두/ 산타는 상우하좌(0,2,4,6번 idx)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(p):
    num,x,y=map(int,input().split())
    graph[x-1][y-1]=num

def find_santa(rx,ry):
    santaList=[]
    for i in range(n):
        for j in range(n):
            if graph[i][j]>0: #산타존재
                distance = abs(i - rx ) ** 2 + abs(j - ry) ** 2
                santaList.append((distance,i,j))

    santaList.sort(key=lambda x: (x[0],-x[1],-x[2]))
    return santaList

def move_rudolph(sx,sy):
    global rx,ry
    candidate=[]
    #가까운 쪽 대각선 이동을 어케하지
    for i in range(8):
        nx,ny=rx+direct[i][0], ry+direct[i][1]
        distance=abs(nx - sx) ** 2 + abs(ny - sy) ** 2 #이동한 루돌프 - 산타거리
        candidate.append((distance,nx,ny,i)) #i는 방향
    candidate.sort(key=lambda x: (x[0],-x[1],-x[2]))
    return candidate

def santa_hit_santa(x, y, d, num):
    q=deque()
    q.append((x,y,num))
    while q:
        x,y,value=q.popleft()
        nx,ny=x+direct[d][0], y+direct[d][1]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny]==0:
                graph[nx][ny]=num
            else:
                q.append((nx,ny,graph[nx][ny]))
                graph[nx][ny]=value
        else:
            canSantaMove[num] = 0

def santa_hit_rudolf(num,x,y,d):
    #방향 switch
    if d==0: d=2
    elif d==1: d=3
    elif d==2: d=0
    else: d=1

    nx,ny=x+(D* dx[d]), y+(D* dy[d])

    if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 0:
            graph[nx][ny] = num
        elif graph[nx][ny] > 0:
            santa_hit_santa(nx,ny,d,num)
            graph[nx][ny] = num
        return
    else:
        canSantaMove[num] = 0
        return

def move_santa(x,y):
    global rx, ry
    candidate = []
    distance=abs(x-rx)**2 + abs(y-ry)**2 #현재 산타- 루돌프 거리

    for i in range(4,2):
        nx, ny = x + dx[i], y + dy[i]
        dist = abs(nx - rx) ** 2 + abs(ny - ry) ** 2  # 이동한 산타 - 루돌프
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if graph[nx][ny]<=0 and dist<distance:
            distance=dist
            candidate.append((distance, nx, ny, i))  # i는 방향
    candidate.sort(key=lambda x: x[0])
    return candidate

def rudolf_hit(x,y,d,num):
    nx,ny=x+ (c* direct[d][0]), y+ (c* direct[d][1])
    if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 0:
            graph[nx][ny] = num
        else:
            santa_hit_santa(nx,ny,d,graph[nx][ny])
            graph[nx][ny] = num
    else:
        canSantaMove[num] = 0

for idx in range(m):
    if sum(canSantaMove)==0:
        break

    #가까운 산타 위치 찾고 루돌프 이동
    santaList=find_santa(rx,ry)
    distance,x,y=santaList[0]
    graph[rx][ry]=0

    rudolfMovement=move_rudolph(x,y)
    dist,rx,ry,d=rudolfMovement[0]

    #루돌프가 산타와 부딪히면
    num=graph[rx][ry]
    if num>0:
        koSanta[num] = 2 #기절 상태.
        score[num] +=c #score[산타Num] 점수 얻기
        rudolf_hit(rx,ry,d,num)

    graph[rx][ry]=-1

    santaPos=[]
    for i in range(n):
        for j in range(n):
            if graph[i][j]>0:
                santaPos.append((graph[i][j], i, j))
    santaPos.sort(key=lambda x: x[0]) #산타 순서대로 정렬

    for z in range(1,p+1):
        sx,sy=-1,-1
        for i in range(n):
            for j in range(n):
                if graph[i][j]==z:
                    sx,sy=i,j #산타 좌표 찾기
        if sx==-1 and sy==-1:
            continue
        number=graph[sx][sy]
        if koSanta[number] !=0: #기절한 산타 pass
            continue

        santaMovement=move_santa(sx,sy)
        if len(santaMovement)==0:
            continue

        graph[sx][sy]=0
        dist,sx,sy,d=santaMovement[0]
        if graph[sx][sy]==0:
            graph[sx][sy]=number
        elif graph[sx][sy]==-1: #루돌프 위치
            score[number]+=D
            koSanta[number]=2
            santa_hit_rudolf(number,sx,sy,d) #d 반대 방향

    for i in range(1,p+1):
        if canSantaMove[i]==1:
            score[i]+=1
    for i in range(1,p+1):
        if koSanta[i]>0:
            koSanta[i]-=1

print(*score[1:])

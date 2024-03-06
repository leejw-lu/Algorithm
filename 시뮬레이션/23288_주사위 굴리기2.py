from collections import deque
n,m,k=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

dice=[2,4,1,3,5,6] #주사위 맨 밑칸 dice[-1]
dx=[0,1,0,-1] #동남서북
dy=[1,0,-1,0]

d=0 #이동방향 idx (동남서북 0123)
x,y=0,0 #->첨에 1,1로 해서 엉망
totalScore=0

def checkScore(x,y,point):
    q=deque() #q 여기서 세팅하기
    q.append((x,y))
    visited=[[False]*(m) for _ in range(n)] #m_ n 주의!!!!
    visited[x][y]=True
    count=1

    while q:
        x,y=q.popleft()
        #count+=1 여기서 쓰려면 count=0 초기화해야함.
        for i in range(4):
            nx,ny=x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if point==graph[nx][ny] and not visited[nx][ny]:
                count+=1
                q.append((nx,ny)) 
                visited[nx][ny]=True #방문표시 해야함!!!

    return point*count

#d 방향으로 주사위 이동시키기
def moveDice(d):
    #tmp=dice[5] 
    if d==0: #동
        # dice[5]=dice[3]
        # dice[3]=dice[2]
        # dice[2]=dice[1]
        # dice[1]=tmp
        dice[5],dice[3],dice[2],dice[1]=dice[3],dice[2],dice[1],dice[5]
    elif d==1: #남
        dice[5],dice[4],dice[2],dice[0]=dice[4],dice[2],dice[0],dice[5]
    elif d==2: #서
        dice[5],dice[1],dice[2],dice[3]=dice[1],dice[2],dice[3],dice[5]
    else: #북
        dice[5],dice[0],dice[2],dice[4]=dice[0],dice[2],dice[4],dice[5]


for i in range(k):
    #1. 이동방향으로 한칸 굴러가기
    nx,ny= x+dx[d], y+dy[d]
    if nx<0 or nx>=n or ny<0 or ny>=m:
        d=(d+2)%4 #방향 바꾸기
        nx,ny= x+dx[d], y+dy[d]

    #2. 점수 획득하기
    point=graph[nx][ny]
    totalScore+=checkScore(nx,ny,point)

    #3. 주사위 이동 후 이동방향 결정하기
    moveDice(d)
    if dice[-1]> point: 
        d=(d+1)%4       #시계방향
    elif dice[-1]< point:
        d=(d+3)%4       #반시계방향

    x,y=nx,ny  #x,y세팅 해야함!!!!!

print(totalScore)



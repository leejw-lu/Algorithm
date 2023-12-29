import sys
read=sys.stdin.readline

dx = [0,-1,0,1] #동북서남 (x,y 방향 주의!!!!)
dy = [1,0,-1,0]
airCleaner=[]
result=0

#r과 c 범위가 매우 작기 때문에 미리 먼지 위치 append 안해도 된다.
#1. 미세먼지 확산 -> "동시성"
def spread():
    temp=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j]!=0 and graph[i][j]!=-1:
                dust=0
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<r and 0<=ny<c and graph[nx][ny]!=-1:
                        temp[nx][ny]+=graph[i][j]//5
                        dust+=graph[i][j]//5
                graph[i][j]-=dust
    #graph+ temp 배열 합치기 (동시성)
    for i in range(r):
        for j in range(c):
            graph[i][j]+=temp[i][j]

#2. 공기청정기 위쪽: 동->북->서->남
def clean_up(): 
    d=0 #동 부터 시작
    before=0
    x,y=airCleaner[0],1 #로봇 다음칸

    while True:
        nx=x+dx[d]
        ny=y+dy[d]
        if nx<0 or nx>=r or ny<0 or ny>=c:
            d=(d+1)%4
            continue
        if x==airCleaner[0] and y==0:
            break

        graph[x][y],before = before,graph[x][y]
        x,y=nx,ny
           
#3. 공기청정기 아래쪽: 동->남->서->북
def clean_down():
    d=0 #동 부터 시작
    before=0
    x,y=airCleaner[1],1 #로봇 다음칸

    while True:
        nx=x+dx[d]
        ny=y+dy[d]
        if nx<0 or nx>=r or ny<0 or ny>=c:
            d=(d-1)%4
            continue
        if x==airCleaner[1] and y==0:
            break

        graph[x][y],before = before,graph[x][y]
        x,y=nx,ny

#___________________main
r,c,t=map(int,read().split())
graph=[list(map(int,read().split())) for _ in range(r)]

#공기청정기 위치 찾기
for i in range(r):
    if graph[i][0]==-1:
        airCleaner.append(i)

for _ in range(t):
    spread()
    clean_up()
    clean_down()

#미세먼지 출력
for i in range(r):
    for j in range(c):
        if graph[i][j]>0:
            result+=graph[i][j]
print(result)


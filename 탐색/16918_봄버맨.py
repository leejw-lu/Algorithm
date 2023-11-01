import sys
from collections import deque
read=sys.stdin.readline

dirX=[-1,1,0,0]
dirY=[0,0,-1,1]

def bomb_bfs(): #폭탄 터짐
    while q:
        x,y=q.popleft()
        graph[x][y]='.'
        for i in range(4):
            newX=dirX[i]+x
            newY=dirY[i]+y
            if newX<0 or newX>=R or newY<0 or newY>=C:
                continue
            if graph[newX][newY]=='O': #인접 폭탄 파괴
                graph[newX][newY]='.' #연쇄반응 없으므로 append는 X

def bomb_insert(): #폭탄 찾아 append하기
    for i in range(R):
        for j in range(C):
            if graph[i][j]=='O':
                q.append((i,j))

#---입력
R,C,N=map(int,read().split())

graph=[]
for i in range(R):
    graph.append(list(read().rstrip()))


N=N-1 #처음 1초 가만히 있는 시간 빼기
while N: #원래 N이 2이상
    q=deque()
    bomb_insert() # 1.폭탄 찾아 append하기
    graph = [['O']*C for _ in range(R)] #2.전체 폭탄 세팅(.부분 모두 O)
    N-=1
    if N==0:
        break
    bomb_bfs() #3.폭탄 터트리기
    N-=1

for i in graph:
    print(''.join(i))
#Pypy3로 풀어야 시간초과 X
import sys
read=sys.stdin.readline

N,M,R=map(int,read().split())
graph=[list(map(int, read().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N,M)//2):
        x,y=i,i
        value=graph[x][y]

        #1. 왼쪽 아래로 v
        for j in range(i+1, N-i): 
            x=j
            tmp=graph[x][y] #현재 값 저장
            graph[x][y]=value #이전 값 넣기
            value=tmp

        #2. 아래 오른쪽으로 ->
        for j in range(i+1, M-i): 
            y=j
            tmp=graph[x][y]
            graph[x][y]=value
            value=tmp

        #3. 오른쪽 위로 ^
        for j in range(i+1,N-i):
            x=N-j-1
            tmp=graph[x][y]
            graph[x][y]=value
            value=tmp

        #4. 위쪽 왼쪽으로 <-
        for j in range(i+1,M-i):
            y=M-j-1
            tmp=graph[x][y]
            graph[x][y]=value
            value=tmp

for i in graph:
    print(*i)

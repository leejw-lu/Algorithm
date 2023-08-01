import sys
sys.setrecursionlimit(1000000) #10000보다 크게 해야 성공
read=sys.stdin.readline

N,M=map(int,read().split()) #세로i, 가로j

dirX=[1,-1,0,0]
dirY=[0,0,1,-1]

def dfs(x,y):
    global graph, count

    graph[x][y]=False
    count+=1

    for i in range(4):
        newX=x+dirX[i]
        newY=y+dirY[i]
        if newX<0 or newX>=N or newY<0 or newY>=M:
            continue
        if graph[newX][newY]:
            dfs(newX,newY)


#graph 정보 -> 공백있게
graph=[]
for _ in range(N):
    graph.append(list(map(int,read().split())))

result=[]
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            count=0
            dfs(i,j)
            result.append(count)
            
print(len(result)) #그림 개수

if len(result):
    print(max(result)) #가장 넓은 그림
else:
    print(0)

# list 배열에 값이 업을 경우 max함수 쓰면 오류남.

import sys
read=sys.stdin.readline

N=int(read())
#matrix=[list(map(int, read())) for _ in range(n)]

dirX=[1,-1,0,0]
dirY=[0,0,1,-1]

def dfs(x,y):
    global graph, count

    graph[x][y]=False
    count+=1

    for i in range(4):
        newX=x+dirX[i]
        newY=y+dirY[i]
        if newX < 0 or newX >= N or newY < 0 or newY >= N:
            continue
        if graph[newX][newY]:
            dfs(newX,newY)

#graph 정보 -> 공백없이
graph = []
for i in range(N):
   graph.append(list(map(int, input())))

count=0 #각 단지내 집의 수
result=[]

for i in range(N):
      for j in range(N):
        if graph[i][j] :
            dfs(i,j)
            result.append(count)
            count=0 #리셋해주기

print(len(result)) #총 단지수 -> 그냥 len(result)해도 되네.
result.sort()
for num in result:
    print(num)

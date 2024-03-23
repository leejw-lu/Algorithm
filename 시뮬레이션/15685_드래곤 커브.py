n=int(input())
graph=[[0]*101 for _ in range(101)]

#d=0,1,2,3
dx=[0,-1,0,1] #y좌표 #->, ^, <-, v 방향
dy=[1,0,-1,0] #x좌표

#90도 시계방향
#   d=(d+1)%4   
#   x=x+dx[d]

for i in range(n):
    y,x,d,g=map(int, input().split())
    graph[x][y]=1

    #커브 리스트
    curve=[d]
    for _ in range(g):
        for k in range(len(curve)-1,-1,-1): #len(curve)~0까지, 거꾸로.
            curve.append((curve[k]+1)%4)  #2세대: [0,1,2,1]
    
    #드래곤 커브 만들기
    for j in range(len(curve)):
        x+=dx[curve[j]] #x += dx[curve[j]]
        y+=dy[curve[j]]
        if x<0 or x>=101 or y<0 or y>=101:
            continue
        graph[x][y]=1

result=0
for i in range(100):
    for j in range(100):
        #네 꼭짓점 모두 1
        if graph[i][j]==1 and graph[i+1][j]==1 and graph[i][j+1]==1 and graph[i+1][j+1]==1:
            result+=1
print(result)

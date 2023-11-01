import sys
read=sys.stdin.readline

dirX=[-1,-1,0,1,1,1,0,-1]
dirY=[0,1,1,1,0,-1,-1,-1]

N=int(read())
graph=list(read().rstrip() for _ in range(N))
graph2=list(read().rstrip() for _ in range(N))
result=[['.'] * N for _ in range(N)]

flag=False #지뢰 선택 여부

for i in range(N):
    for j in range(N):

        #사용자가 지뢰 안눌렀을 때
        if graph2[i][j]=='x' and graph[i][j]=='.':
            count=0
            for k in range(8):
                newX=i+dirX[k]
                newY=j+dirY[k]
                if newX<0 or newX>=N or newY<0 or newY>=N:
                    continue
                if graph[newX][newY]=='*':
                    count+=1
            result[i][j]=count

        #사용자가 지뢰 눌렀을 때
        if graph[i][j] == '*' and graph2[i][j] == 'x':
            flag=True

if flag:
    for i in range(N):
        for j in range(N):
            if graph[i][j]=='*':
                result[i][j]='*'

#출력
for i in result:
    for j in i:
        print(j,end='')
    print()
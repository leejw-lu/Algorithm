from collections import deque
n=int(input())
graph=[[0]*n for _ in range(n)] #교실배치
student=[]
#visited=[False]*(n**2)
visited=[[0,0]] *(n**2) #배치 번호
arr=[False]*(n**2)

dx=[1,0,-1,0] #북동남서
dy=[0,1,0,-1]

#인접한 칸 중 비어있는 칸 가장 많은 곳 배치

#1번 조건
def find_student(num, pos):
    global tmp
    x,y=pos[0],pos[1]

    for i in range(4):
        nx,ny=x+dx[i], y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if graph[x][y]==0: #graph[][]==0이렇게 되면 8번 학생에서 tmp[nx][ny]=2 가 못된다. 2. 이 if조건 없으면 이미 배치된것도 +된다.
            tmp[nx][ny] += 1

    #return tmp
    #print("tmp: ", tmp)


def count_seat():
    global tmp
    value=0
    near=deque()

    for i in range(n):
        for j in range(n):
            if tmp[i][j]==0: continue
            if tmp[i][j]>value:
                value=tmp[i][j]
            #value=max(value, tmp[i][j])

    for i in range(n):
        for j in range(n):
            if tmp[i][j]==value:
                near.append((i,j)) #좌표

    return near


#2번 조건
def select_candidate(near): #
    candidate=[]

    while near:
        count=0
        x,y=near.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                count += 1
        candidate.append((count, x, y)) #인접한 칸 개수, x좌표, y좌표

    #3번 조건 정렬
    candidate.sort(key=lambda x: (-x[0],x[1],x[2]))
    #최종 자리 선택== candidate[0]의 [1],[2]번 index
    return candidate


#입력
for i in range(n**2):
    num,a,b,c,d=map(int,input().split())
    student.append([num-1,a-1,b-1,c-1,d-1])

#첫번째 학생 배치 (항상 1,1)
num=student[0][0]
graph[1][1]=student[0][0]
visited[num]=[1,1]


#근데 좋아하는 친구 4명 모두 자리 안앉아있을 경우도 있을 텐데,,,, 첫번째 친구처럼...

for i in range(1, n**2):
    num=student[i][0]
    print("num: ", num)
    #visited[num]=True

    tmp = [[0] * n for _ in range(n)]
    for j in range(4):
        favoriteSt=student[i][j+1]
        if visited[favoriteSt] != [0,0]:
            #1번 조건
            find_student(favoriteSt, visited[favoriteSt])

    print("for문 끝난 tmp: ", tmp)
            #candidate=bfs(favoriteSt, visited[favoriteSt])

    #1번 조건 결과 확인
    near=count_seat()
    print("near: ", near)
    print("graph: ", graph)

    if len(near)>1:
        #조건 2 & 3
        candidate=select_candidate(near)
        print("candidate ", candidate)
        x,y=candidate[0][1],candidate[0][2]
        graph[x][y]=num
        visited[num]=[x,y]
    else:
        x, y = near.popleft()
        graph[x][y] = num
        visited[num] = [x, y]

    print("1타임 끝")

print("====자리 배치 끝=====")
print("graph: ", graph)










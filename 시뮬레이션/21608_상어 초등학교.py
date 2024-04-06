n=int(input())
graph=[[0]*n for _ in range(n)] #교실 배치
students = [list(map(int, input().split())) for _ in range(n**2)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

#첫번째 학생 배치 (항상 1,1)
graph[1][1]=students[0][0]

for _ in range(1, n**2):
    num=students[_][0] #-> 나중에 실제 배치 좌표로 변경
    student=students[_][1:] #좋아하는 학생
    candidate=[]

    for i in range(n):
        for j in range(n):
            if graph[i][j]==0: #자리 빈칸
                like=0
                blank=0 #빈 자리 수
                for k in range(4):
                    nx,ny=i+dx[k], j+dy[k]
                    if nx<0 or nx>=n or ny<0 or ny>=n:
                        continue
                    #탐색 위치에 좋아하는 친구 있으면
                    if graph[nx][ny] in student:
                        like+=1
                    if graph[nx][ny]==0:
                        blank+=1
                candidate.append([like, blank, i, j])

    #좋아하는 친구 수(내림), 인접한 칸 개수(내림), x좌표(오름), y좌표(오름)
    candidate.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    x,y=candidate[0][2], candidate[0][3]
    graph[x][y]=num

#만족도 검사
result=0
students.sort()

for i in range(n):
    for j in range(n):
        count=0 #현재 학생의 행복도
        num=graph[i][j] #학생 번호
        for k in range(4):
            nx,ny=i+dx[k], j+dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny] in students[num-1][1:]:
                count+=1

        if count!=0:
            result+=(10** (count-1)) #1->1점/ 2->10점/ 3->100점/ 4->1000점

print(result)

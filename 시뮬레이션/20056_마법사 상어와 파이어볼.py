import sys
read=sys.stdin.readline

#0~7 방향
dir=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

#이동 끝난 후 2개 이상 파이어볼 있는 칸 합치고 4개로 쪼개기
def checkFireBall():
    for i in range(n):
        for j in range(n):
            if len(graph[i][j])>1:
                sum_m, sum_s, count, odd, even= 0, 0, len(graph[i][j]), 0, 0
                #for m,s,d in graph[i][j]: ->반복돼서 X
                while graph[i][j]:
                    m,s,d= graph[i][j].pop(0) #graph 비우기
                    sum_m+=m
                    sum_s+=s
                    #방향 홀.짝 count
                    if d%2 : odd+=1 
                    else: even+=1
                #파이어볼 4개로 나누기
                if count==odd or count==even : #모두 홀or짝
                    nd=[0,2,4,6] #방향
                else:
                    nd=[1,3,5,7]
                if sum_m//5: #질량 0이면 소멸
                    for d in nd:
                        fireballs.append([i,j,sum_m//5,sum_s//count,d])
            
            # 1개인 경우
            if len(graph[i][j]) == 1:
                fireballs.append([i, j] + graph[i][j].pop())

n,m,k=map(int,read().split())
graph=[[[] for _ in range(n)] for _ in range(n)]
fireballs=[]

for _ in range(m):
    r,c,m,s,d=map(int,read().split())
    fireballs.append([r-1,c-1,m,s,d])

for _ in range(k):
    #파이어볼 이동
    while fireballs:
        cr,cc,cm,cs,cd= fireballs.pop(0)
        nx=(cr+ dir[cd][0] *cs) %n #1번-N번 연결 (d방향 s만큼 이동)
        ny=(cc+ dir[cd][1] *cs) %n
        graph[nx][ny].append([cm,cs,cd])
    checkFireBall()

#파이어볼 질량 합 구하기
print(sum([f[2] for f in fireballs]))

#graph는 checkFireBall함수에서 pop하니까 모두 비어있음. -> fireballs에서 질량구하기
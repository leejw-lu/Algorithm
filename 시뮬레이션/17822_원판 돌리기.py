n,m,t=map(int,input().split())
disk=[list(map(int,input().split())) for _ in range(n)]

#idx행 d방향 k만큼 회전 함수
def moveDisk(idx,d,k):
    global disk
    for _ in range(k):
        newDisk=[0]*m 
        if d==0: #시계
            for i in range(m):
                newDisk[i]=disk[idx][(i+m-1)%m] #point1: m이 항상 4가 아님!!!!
        else: #반시계
            for i in range(m):
                newDisk[i]=disk[idx][(i+1)%m]
        disk[idx]=newDisk 

#인접하면서 수 같은 것 찾는 함수
def adjSame():
    flag=False
    graph = [[disk[i][j] for j in range(m)] for i in range(n)] #배열복사

    dx=[0,1]
    dy=[1,0]
    
    for i in range(n):
        for j in range(m):
            # #가로 인접 검사
            # if j+1<m and disk[i][j]==disk[i][j+1] and disk[i][j]>0 and disk[i][j+1]>0:
            #     flag=True
            #     graph[i][j],graph[i][j+1]= -1,-1 #-1로 지우기
            # #세로 인접 검사
            # if i+1<n and disk[i][j]==disk[i+1][j] and disk[i][j]>0 and disk[i+1][j]>0: #if tmp=disk[i][j]
            #     flag=True
            #     graph[i][j],graph[i+1][j]= -1,-1 #-1로 지우기

            for k in range(2):
                nx, ny= i+dx[k], (j+dy[k])%m    #point2: 원판이니까 끝행 이어주기
                # point3: graph가 아닌 disk로 if문 판별해야함!!!!!
                if 0<=nx<n and 0<=ny<m and disk[i][j] != 0 and disk[i][j] == disk[nx][ny] : 
                    graph[nx][ny]=0
                    graph[i][j]=0
                    flag=True
    
    #print("flag: ", flag)
    if not flag:
        count,sum=0,0
        for i in range(n):
            for j in range(m):
                sum+=disk[i][j]
                if disk[i][j]:
                    count+=1

        if count==0: return #point4: 이거 해줘야함!!!!!!! 안그럼 0으로 나누는 상황발생
        avg=sum/count #float
        for i in range(n):
            for j in range(m):
                if graph[i][j]==0: continue #point5: 이거 해야함. 아니면 graph==-1이 0이 된다.
                if avg>disk[i][j]: graph[i][j]+=1
                elif avg<disk[i][j]: graph[i][j]-=1 #같은 경우는 조건에 없음.
    
    #print("찐 최종 disk: ", disk)
    for i in range(n):
        for j in range(m):
            disk[i][j]=graph[i][j]
            
for _ in range(t):
    x,d,k=map(int,input().split())
    #x배수
    for i in range(1,n):
        tmp=x*i
        if tmp>n: break
        idx=tmp-1
        moveDisk(idx,d,k) # disk 회전하기
    #print("최종 이동 후 disk: ", disk)
    adjSame()

result=0
for d in disk:
    result+=sum(d)
print(result)
n=int(input())
target=int(input())
target_x,target_y=0,0

dx=[0,1,0,-1] #우하좌상
dy=[1,0,-1,0] 

graph=[[0]*n for _ in range(n)]
mid=n//2
x,y,layer=mid,mid,mid

k=2
cnt=0 #2, 4, 6, ...
graph[x][y]=1
if target==1:  #이거 추가해야함!!!
    target_x,target_y=mid+1,mid+1

for _ in range(layer): #껍데기 몇번 반복
    if k==2:
        nx,ny=x-1, y-1
    else:
        nx,ny=nx-1, ny-1
    
    cnt+=2 #+2, +4, +6
    for l in range(4):  #우하좌상
        for _ in range(cnt):
            nx=nx+dx[l]
            ny=ny+dy[l]
            graph[nx][ny]=k
            if k==target:
                target_x,target_y=nx+1, ny+1
            k+=1

#출력
for v in graph:
    print(*v)
print(target_x,target_y)
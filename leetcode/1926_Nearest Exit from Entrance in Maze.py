from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n=len(maze)
        m=len(maze[0])
        #visited=[[-1] * n for _ in range(m)]
        
        q=deque()
        q.append((entrance[0],entrance[1],0))
        maze[entrance[0]][entrance[1]]= "+" #입구 방문표시 해야함.

        dx=[-1,1,0,0]
        dy=[0,0,-1,1]

        while q:
            x,y,d=q.popleft()
            for i in range(4):
                nx, ny= x+dx[i], y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if maze[nx][ny]=="." :
                    if nx==0 or nx==n-1 or ny==0 or ny==m-1:
                        return d+1
                    q.append((nx,ny, d+1))
                    maze[nx][ny]="+" #방문표시
        return -1
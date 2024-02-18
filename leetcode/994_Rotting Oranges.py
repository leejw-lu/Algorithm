from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m= len(grid), len(grid[0])
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]

        q=deque()

        #rotten orange q에 append
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))

        #rotten orange 퍼트리기
        while q:
            x,y=q.popleft()
            for i in range(4):
                nx,ny= x+dx[i], y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if grid[nx][ny] ==1:
                    grid[nx][ny]=grid[x][y]+1
                    q.append((nx,ny))

        #검사하기
        result=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1: #fresh orange
                    return -1
                result=max(result,grid[i][j])

        if result >= 2:
            return result-2
        else:
            return result
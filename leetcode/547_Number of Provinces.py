class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=[False]*len(isConnected)

        def dfs(idx):
            visited[idx]=True
            for next in range(len(isConnected)):
                if not visited[next] and isConnected[idx][next]:
                    dfs(next)
        
        answer=0
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                answer+=1
        return answer
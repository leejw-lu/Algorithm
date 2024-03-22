def dfs(start, graph, visited, checkLink):
    count=1
    visited[start]=True
    for next in graph[start]:
        if not visited[next] and checkLink[start][next]:
            count+=dfs(next, graph, visited, checkLink)
    return count

def solution(n, wires):
    answer = float("inf")
    
    #끊은 간선인지 체크
    checkLink=[[True]*(n+1) for _ in range(n+1)]
    graph=[[] for _ in range(n+1)]
    
    for x,y in wires:
        graph[x].append(y)
        graph[y].append(x)
    
    for x,y in wires:
        visited=[False]*(n+1)
        checkLink[x][y]=False #a-b 간선 끊기
        cntX=dfs(x,graph,visited,checkLink)
        cntY=dfs(y,graph,visited,checkLink)
        checkLink[x][y]=True
        
        answer=min(answer,abs(cntX-cntY))
    
    return answer
#상향식 풀이

import sys
read=sys.stdin.readline

#입력
N= int(read())

graph = []
for i in range(N):
  graph.append(list(map(int, input().split())))

for i in range(N-2,-1,-1): #i=n-2 ~ i>=0 까지 i --
  for j in range(i+1): # j=0 ~ j<=i 까지 j++
    graph[i][j]+=max(graph[i+1][j],graph[i+1][j+1])

print(graph[0][0])
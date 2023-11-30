#https://velog.io/@leetaekyu2077/%EB%B0%B1%EC%A4%80-16926%EB%B2%88-%EB%B0%B0%EC%97%B4-%EB%8F%8C%EB%A6%AC%EA%B8%B0-1
#2차원 배열 1차원으로 변형 후 회전 시키기
from sys import stdin
from collections import deque
read=stdin.readline

N, M, R = map(int, read().split())

matrix = []
answer = [[0]*M for _ in range(N)]
deq = deque()

for i in range(N):
    matrix.append(list(read().split()))

loops = min(N, M) // 2
for i in range(loops):
    deq.clear()
    deq.extend(matrix[i][i:M-i])
    deq.extend([row[M-i-1] for row in matrix[i+1:N-i-1]])
    deq.extend(matrix[N-i-1][i:M-i][::-1])
    deq.extend([row[i] for row in matrix[i+1:N-i-1]][::-1])
    
    deq.rotate(-R)
    
    for j in range(i, M-i):                 # 위쪽
        answer[i][j] = deq.popleft()
    for j in range(i+1, N-i-1):             # 오른쪽
        answer[j][M-i-1] = deq.popleft()
    for j in range(M-i-1, i-1, -1):           # 아래쪽
        answer[N-i-1][j] = deq.popleft()  
    for j in range(N-i-2, i, -1):           # 왼쪽
        answer[j][i] = deq.popleft()    

for line in answer:
    print(" ".join(line))

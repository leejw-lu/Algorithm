import sys
from collections import deque
read=sys.stdin.readline

T=int(read())
for _ in range(T):
  N,M= map(int,read().split())
  q = deque(list(map(int,read().split()))) #list 안해도 되려나..? 해보기
  index = deque(list(range(N)))
  #print(q)

  count=0
  while q:
    max_q= max(q)
    num= q.popleft()
    idx= index.popleft()

    if (max_q>num):
      q.append(num)
      index.append(idx) #인덱스도 넣어주기
    else:
      count+=1
      if (idx==M):
        print(count)
        break

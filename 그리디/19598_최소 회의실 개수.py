import sys, heapq
read=sys.stdin.readline

N=int(read())
time=[]

for _ in range(N):
    start,end=map(int,read().split())
    time.append([start,end])

time.sort(key=lambda x: x[0]) #[[0, 40], [5, 10], [15, 30]]
count=1
room=[]
heapq.heappush(room, time[0][1])

for i in range(1,N):
    if time[i][0]>=room[0]: #시작시간이 끝나는 시간보다 느리거나 같은 경우
        heapq.heappop(room)
    else:
        count+=1
    heapq.heappush(room,time[i][1])

print(count)
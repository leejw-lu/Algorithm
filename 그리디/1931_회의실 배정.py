import sys
read=sys.stdin.readline

N=int(read())
time=[]
for i in range(N):
    start, end=map(int,read().split())
    time.append([start,end])

#1순위: 끝나는 시간[1], 2순위: 시작하는 시간[0]
time.sort(key=lambda x:(x[1],x[0]))

count=0
last=0 #회의 마지막 시간 저장

for i, j in time:
    if i>=last:
        count+=1
        last=j

print(count)

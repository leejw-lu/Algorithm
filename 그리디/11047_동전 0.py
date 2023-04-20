import sys
read=sys.stdin.readline

N,K= map(int,read().split())

data=[int(read()) for _ in range(N)]

count=0
for i in reversed(range(N)):
    count +=K//data[i]
    K= K % data[i]

print(count)
            
import sys
read=sys.stdin.readline

n,m=map(int,read().split())
arr=list(map(int,read().split()))
dp=[0]
sum=0

for i in range(n):
    dp.append(dp[i]+arr[i])

for _ in range(m):
    a,b=map(int, read().split())
    print(dp[b]-dp[a-1])
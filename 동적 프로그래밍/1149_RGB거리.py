import sys
read=sys.stdin.readline

N=int(read())
dp=[]
for _ in range(N):
    dp.append(list(map(int,read().split())))

for i in range(1,N):
    dp[i][0]=min(dp[i-1][1],dp[i-1][2])+ dp[i][0] #빨 Ex) 49+ min(42,83)
    dp[i][1]=min(dp[i-1][0],dp[i-1][2])+ dp[i][1] #초 Ex) 60+ min(26,83)
    dp[i][2]=min(dp[i-1][0],dp[i-1][1])+ dp[i][2] #파 Ex) 57+ min(26,42)

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))
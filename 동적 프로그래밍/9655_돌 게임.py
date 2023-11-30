import sys
read=sys.stdin.readline

N=int(read())
dp=[0]*(1001)

dp[1]=1
dp[2]=2
dp[3]=1

for i in range(4,N+1):
    dp[i]=min(dp[i-1],dp[i-3])+1

if dp[N]%2==1: #홀수이면 sk가 이김
    print("SK") 
else:
    print("CY")
import sys
read=sys.stdin.readline

N=int(read())
dp=[0] * (N+1)

for i in range(2,N+1):
    dp[i]=dp[i-1]+1 #dp[7] =dp[6]+1, dp[10]=dp[9]+1

    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1) #dp[9]=ming(dp[8]+1,dp[3]+1) //3연산 1번 더해주기
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1) #dp[N//2]+1에서, +1은 //2 연산1번 더해준 것.
    
print(dp[N])

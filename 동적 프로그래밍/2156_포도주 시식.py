n=int(input())
wine=[0]+[int(input()) for _ in range(n)]
dp=[0]*(n+1)
dp[1]=wine[1]
if n>1:
    dp[2]=wine[1]+wine[2]

for i in range(3,n+1):
            #xox           xoo                      oxo
    dp[i]=max(dp[i-1], wine[i]+wine[i-1]+dp[i-3], wine[i]+dp[i-2])
    #i번째 안마신 경우, i,i-1번째 마시고 i-3번째까지 마신 양, i번째 마시고 i-2번째까지 마신 양
print(dp[n])
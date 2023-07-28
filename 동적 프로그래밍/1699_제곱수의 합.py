import sys
read=sys.stdin.readline

N=int(read())
dp=[0]*(N+1)

for i in range(1,N+1):
    dp[i]=i         #dp=[0,1,2,3,4....N] 초기화
    for j in range(1, i):
        # 제곱수가 i보다 커지면 멈춤
        if j*j > i:
            break
        if dp[i] > dp[i-j*j] + 1: 
            dp[i] = dp[i-j*j] + 1  #dp[4-2*2]+1 =1
print(dp[N])

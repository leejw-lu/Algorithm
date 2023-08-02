import sys
read=sys.stdin.readline

N=int(read())
arr=list(map(int, read().split()))

dp = [0] * N
dp[0] = arr[0]

for i in range(1,N):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
    
print(max(dp))


#d=[]
#sum=0
#for i in range(N-1):
   # if arr[i]>0:
      #  sum+=arr[i]
    #else:
       # d.append(sum)
      #  sum=0

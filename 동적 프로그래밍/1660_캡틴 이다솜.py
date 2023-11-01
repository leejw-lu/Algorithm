#pypy3
import sys
read=sys.stdin.readline

N = int(read())

triangle=[0,1] #1,3,6,10,15 ...
tetrahedron=[0,1] #1,4,10,20,35 ...

for i in range(2,N+1):
    triangle.append(triangle[i-1]+i) #triangel[i]= 해서 하면 indexError남.
    tetrahedron.append(tetrahedron[i-1]+triangle[i])

dp=[3000000 for i in range(N+1)]
dp[0]=0
dp[1]=1

for i in range(2,len(dp)):
    for count in tetrahedron:
        if count>i: #대포알 개수로 사면체를 못 만드는 경우
            break
        if count==i: #대포알 개수==사면체 개수
            dp[i]=1
            break
        dp[i]=min(dp[i], dp[i-count]+1)

print(dp[-1])

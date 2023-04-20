#https://www.acmicpc.net/problem/12865
#NS(n,k)= max |  NS(n-1, k-w[n]) + val(n)
#             |  NS(n-1, k) 

import sys
read= sys.stdin.readline
n, k= map(int, read().split())

WV=[[0,0]]
for i in range(n):
    WV.append(list(map(int, read().split())))
#WV.append(list(map(int, read().split())) for i in range(n))
#WV=[list(map(int, read().split())) for i in range(n)]
# [무게, value] => [[6, 13], [4, 8], [3, 6], [5, 12]] 
ns=[[0 for i in range(k+1)] for j in range(n+1)]

for i in range(1, n+1):
    for j in range(1,k+1):
        w=WV[i][0]
        v=WV[i][1]

        if j<w:
            ns[i][j]=ns[i-1][j]
        else:
            ns[i][j]=max(ns[i-1][j], ns[i-1][j-w]+v)

print(ns[n][k]) #이게 최대 value값.
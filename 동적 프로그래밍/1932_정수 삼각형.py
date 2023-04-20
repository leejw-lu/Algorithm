import sys
read=sys.stdin.readline
MAX=500 +10

#입력
N= int(read())
graph=[[0]* (MAX) for _ in range(MAX)]

for i in range(1,N+1):
    data=list(map(int, read().split()))
    for j in range(i):
        graph[i][j+1]=data[j]
#print(graph)

#최대 합
sum=[[0]* (MAX) for _ in range(MAX)]

for i in range(1,N+1):
    for j in range(1,i+2):  
        a= graph[i][j]
        #print("i와 j", i," " ,j)
        sum[i][j]=max(sum[i-1][j-1],sum[i-1][j]) + a

#출력
count=max(sum[N])
#for i in range(1,N+1):
    #print(sum[N][i])
print(count)
import sys
read=sys.stdin.readline

N=int(read())
arr=list(map(int,read().split()))
arr.sort()

for i in range(N-1): #0,1,2,3 총 4개 index만
    arr[i+1]=arr[i]+arr[i+1]

print(sum(arr))
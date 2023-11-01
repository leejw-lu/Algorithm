import sys
read=sys.stdin.readline

N=int(read())
arr=list(int(read()) for _ in range(N))
arr.sort(reverse=True)

weight=0
for i in range(N):
    if weight<arr[i]*(i + 1):
        weight=arr[i]*(i + 1)

print(weight)
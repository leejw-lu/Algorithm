import sys
read=sys.stdin.readline

N=int(read())
arr=[]
for _ in range(N):
    arr.append(int(read()))
arr.sort(reverse=True)

i=2
while i<N:
    arr[i]=0
    i+=3
print(sum(arr))
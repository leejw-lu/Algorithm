import sys
read=sys.stdin.readline

N=int(read())
arr=list(map(int,read().split()))
arr.sort(reverse=True)

result=arr[0]
#result+= sum(arr[1:]) /2

for i in range(1,N):
    result+=arr[i]/2
print(result)
import sys
read=sys.stdin.readline

N,K = map(int, read().split())
arr=list(read().rstrip())

count=0
for i in range(N):
    if arr[i]=='P':
        for j in range(i-K, i+K+1):
            if 0<= j <N and arr[j]=='H':
                count+=1
                arr[j]='N' #햄버거 삭제
                break
print(count)



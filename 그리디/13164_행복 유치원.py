import sys
read=sys.stdin.readline

N,K=map(int,read().split())
arr=list(map(int,read().split()))
sub=[]

for i in range(N-1):
    sub.append(arr[i+1]-arr[i]) #인접한 키 차이 저장
sub.sort(reverse=True)

result=0
result+=sum(sub[K-1:]) #차이 가장 적은 k-1개 합 구하기
print(result)
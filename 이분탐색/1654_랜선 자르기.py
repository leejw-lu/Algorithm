k,n=map(int,input().split())
arr=list(int(input()) for _ in range(k))

start=1
end=max(arr)

while start <= end:
    mid=(start+end)//2
    count=0     #잘라진 랜선의 길이 개수
    for a in arr:
        count+= a//mid

    if count>=n:
        start=mid+1
    else:
        end=mid-1

print(end)
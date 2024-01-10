import sys
read=sys.stdin.readline

n,m=map(int,read().split())
arr=[int(read()) for _ in range(n)]
arr.sort()

start=1     #공유기 최소 거리
end=arr[-1]-arr[0]  #공유기 최대거리
result=0

#이분탐색: 공유기 설치할 거리
while(start<=end):
    mid=(start+end)//2      #공유기 설치 거리
    current=arr[0]
    count=1
    for i in range(1,len(arr)):
        if arr[i]>=current+mid: #공유기 설치
            count+=1
            current=arr[i]

    if count>=m:  #공유기 간격 넓히기
        start=mid+1
        result=mid
    else:
        end=mid-1 #공유기 간격 좁히기

print(result)
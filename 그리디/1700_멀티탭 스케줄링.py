n,k=map(int,input().split())
arr=list(map(int,input().split()))
plug=[]
result=0 #플러그 빼는 최소 횟수

for i in range(k):
    if arr[i] in plug: #플러그 꽂혀 있으면 pass
        continue
    if len(plug)<n:    #플러그 자리 남아 있으면 꽂기
        plug.append(arr[i])
        continue

    #plug에 안꽂혀있고 자리도 꽉 찼을 때 뽑기
    idxs=[]
    flag=True
    for j in range(n):
        try:
            idx=arr[i:].index(plug[j]) #plug[j]의 index 찾기여서 뒤에 값 없으면 에러 발생할 수도.
        except:
            idx=101 #다음 사용 순서가 없는 경우
            flag=False
        idxs.append(idx)
        if not flag:
            break

    plug_out=idxs.index(max(idxs)) #가장 멀리있는 index
    del plug[plug_out]
    plug.append(arr[i])
    result+=1

print(result)
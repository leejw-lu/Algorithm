import sys
read=sys.stdin.readline

N=int(read())

result=0
for _ in range(N):
    str=read().rstrip()
    arr=list(str)
    count=len(arr)

    for i in range(count-1):
        if arr[i]==arr[i+1]:
            arr[i]='O' #옆과 동일하면 O로 바꾸기

    cO=arr.count('O')
    if cO>0:
        cO-=1 #aaa인 경우, OOa이기 때문에 중복X인 set하면 Oa가 남음.

    arr=set(arr)

    if count==len(arr)+ cO: #중복없음
        result+=1

print(result)
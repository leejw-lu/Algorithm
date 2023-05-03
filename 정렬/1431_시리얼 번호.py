import sys
read=sys.stdin.readline

N=int(read())

arr=[]
for _ in range(N):
    a=read().rstrip() #rstrip을 해줘야 \n없이 출력 가능

    #자리수 합
    sum=0
    for i in a:
        if i.isdigit():
            sum+=int(i)
    arr.append((a,sum))

#정렬기준 1: 짧은 순 2: 자리수 합 작은 순 3: 알파벳 사전 순
arr.sort(key=lambda x: (len(x[0]),x[1],x[0]))

for i in arr:
    print(i[0])


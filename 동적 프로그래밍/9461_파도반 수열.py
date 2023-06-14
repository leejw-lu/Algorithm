import sys
read=sys.stdin.readline

T=int(read())

for _ in range(T):
    N=int(read())
    arr=[1]*100
    arr[3]=arr[4]=2 #초기화

    if N>=5:
        for i in range(5,N):
            arr[i]=arr[i-1]+arr[i-5]

    print(arr[N-1])


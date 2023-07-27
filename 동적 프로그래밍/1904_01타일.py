import sys
read=sys.stdin.readline

N=int(read())

arr=[0] * (N+2)

arr[1]=1
arr[2]=2

if N>2:
    for i in range(3,N+1):
        #arr[i]=arr[i-1]+arr[i-2] -> 메모리 초과(int 범위를 벗어난다.)
        arr[i]=(arr[i-1]+arr[i-2]) % 15746 #나머지를 저장해주기

print(arr[N])
import sys
read=sys.stdin.readline

N=int(read())
A=set(map(int,read().split())) #set을 해주면 시간초과 안뜬다.
M=int(read())
arr=list(map(int,read().split()))

for i in arr:
    print(1) if i in A else print(0)


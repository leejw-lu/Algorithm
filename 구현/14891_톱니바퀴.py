import sys
from collections import deque
input=sys.stdin.readline

def check_right(idx, d):
    if idx>3: #4번째 톱니 확인x
        return
    if arr[idx-1][2]!=arr[idx][6]:
        check_right(idx+1,-d)
        arr[idx].rotate(d)

def check_left(idx, d):
    if idx<0: #1번째 톱니 확인x
        return
    if arr[idx][2]!=arr[idx+1][6]:
        check_left(idx-1,-d)
        arr[idx].rotate(d)

#입력
arr = [deque(list(map(int,input().rstrip()))) for _ in range(4)]
k=int(input())

for _ in range(k):
    num,d=map(int,input().split())
    num-=1 #톱니바퀴 index 구하기 (-1)

    #반대방향 회전
    check_left(num-1,-d)
    check_right(num+1,-d)

    #num번째 톱니 회전(무조건)
    arr[num].rotate(d)

#점수계산
result=0
for i in range(4):
    if arr[i][0]==1:
        result+=2**i #제곱
print(result)
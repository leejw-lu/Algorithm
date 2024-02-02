import sys
from collections import deque
input=sys.stdin.readline

def rotate_wheel(num,d):
    #맞닿아 있는 극: a2번-b6번/ b2번-c6번/ c2번-d6번 
    if num==1:
        if arr[0][2]!=arr[1][6]:
            arr[1].rotate(-d)
            if arr[1][2]!=arr[2][6]:
                arr[2].rotate(d)
                if arr[2][2]!=arr[3][6]:
                    arr[3].rotate(-d)
    if num==2:
        if arr[0][2]!=arr[1][6]:
            arr[0].rotate(-d)
        if arr[1][2]!=arr[2][6]:
            arr[2].rotate(-d)
            if arr[2][2]!=arr[3][6]:
                arr[3].rotate(d)
    if num==3:
        if arr[2][2]!=arr[3][6]:
            arr[3].rotate(-d)
        if arr[1][2]!=arr[2][6]:
            arr[1].rotate(-d)
            if arr[0][2]!=arr[1][6]:
                arr[0].rotate(d)
    if num==4:
        if arr[2][2]!=arr[3][6]:
            arr[2].rotate(-d)
            if arr[1][2]!=arr[2][6]:
                arr[1].rotate(d)
                if arr[0][2]!=arr[1][6]:
                    arr[0].rotate(-d)

    arr[num-1].rotate(d) #나중에 rotate하기

#입력
arr = [deque(list(map(int,input().rstrip()))) for _ in range(4)]
k=int(input())

for _ in range(k):
    num,d=map(int,input().split())
    rotate_wheel(num,d)

result=0
for i in range(4):
    if arr[i][0]==1:
        result+=2**i #제곱
print(result)

#파이썬 배열 1칸씩 이동
#시계방향 회전
#deque에서 rotate(1)하면 오른쪽으로 이동, rotate(-1)하면 왼쪽으로 이동
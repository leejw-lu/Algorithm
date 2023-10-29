import sys
read=sys.stdin.readline

arr=read().rstrip().split('.')

for i in range(len(arr)):
    count=len(arr[i])
    if count:
        if count%2: #홀수
            print(-1)
            exit(0)
        else:
            if count%4==0: #4의 배수 AAAA
                arr[i]='AAAA'*(count//4)
            else:           #2의 배수 BB추가
                arr[i]='AAAA'*(count//4)+'BB'
print('.'.join(arr))

#--------sol2 : replace 함수로 간단하게 사용할 수 O
board = read().rstrip()
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)
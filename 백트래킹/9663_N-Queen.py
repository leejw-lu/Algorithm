import sys
read=sys.stdin.readline

N=int(read())
count=0
col = [0] * (N + 1)

def is_promising(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x] - col[i]) == x - i:  #열과 대각선 비교
            return False
    return True

def n_queens(x):
    global count
    if x == N:  # (N=4일때) i=0시작~ i=3, n=4: 끝까지 옴.
        count += 1
        return
    else:
        for i in range(N):
            col[x] = i
            if is_promising(x):
                n_queens(x+1)
n_queens(0)
print(count)

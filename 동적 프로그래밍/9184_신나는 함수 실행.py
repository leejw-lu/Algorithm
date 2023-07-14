import sys
read=sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c] :
        return dp[a][b][c]
    if a<b<c :
        dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
    else:
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

    return dp[a][b][c]

#50, 50, 50 등 재귀 오래걸린 이유는 동일한 값을 계속 연산했기 때문 -> 배열 만들어 return
dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]

while True:
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c))) #format 이용해서 쉽게 print
    
    #print("w("+str(a)+",",str(b)+",",str(c)+") =",w(abc[0],abc[1],abc[2]))


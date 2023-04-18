import sys
read=sys.stdin.readline

N=int(read())
V=[0]
F=[0] * 301

#계단 점수 입력
for _ in range(N):
    V.append(int(read()))
V.append(0)  #이걸 해줘야 Index Error 안난다.

F[0]=0
F[1]=F[0]+V[1]
F[2]=max(F[0], F[1])+ V[2]

for n in range(3,N+1):
    F[n]=max(F[n-3]+V[n-1], F[n-2]) + V[n] #연속된 세 개의 계단을 모두 밟아서는 안 된다.
    #print("n:" , n, "F[n]",F[n])

print(F[N])


import sys
read=sys.stdin.readline

N=int(read())
s=read().rstrip()

colors={'B':0, 'R':0}
colors[s[0]]+=1
for i in range(1,N):
    if s[i] !=s[i-1]:
        colors[s[i]]+=1

result=min(colors['B'], colors['R']) +1 #처음 전체 칠하기1 더해주기
print(result)


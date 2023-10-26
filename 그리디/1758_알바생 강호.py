import sys
read=sys.stdin.readline

N=int(read())
tip=[]

for _ in range(N):
    tip.append(int(read()))
tip.sort(reverse=True)

sum=0
for i in range(len(tip)):
    if tip[i]-i<0:  #tip[i]-(i+1 -1) => tip[i]-i
        break
    sum+=tip[i]-i

print(sum)



#삼성 SW 역량테스트 2015 하반기 1번 문제
import sys
read=sys.stdin.readline

n=int(read())
user=list(map(int,read().split()))
leader,teamone=map(int,read().split())

count=n

for i in range(n):
    user[i]-=leader
    if user[i]>0:
        if user[i]>teamone:
            count+=user[i]//teamone
            if user[i]%teamone > 0:
                count+=1
        else:
            count+=1
print(count)
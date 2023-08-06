import sys
read=sys.stdin.readline

A,B=map(int,read().split())

count=0
while A<B:
    if B % 2 : #나머지O-> 홀수
        if(B%10)==1: #끝자리 1이면 1빼기
            str_b=str(B)
            B=int(str_b[:-1])
        else:
            break        
    else: #짝수
        B= B//2
    
    count+=1

if A==B:
    print(count+1)
else:
    print(-1)
import sys
read=sys.stdin.readline

N=int(read())
count=0

if N<5:
    if N%2==0:
        count=N//2
    else:
        count=-1
else: # N이 5 이상
    if N%5==0:
        count=N//5
    elif (N%5)%2==0: #5로 나눈 나머지가 짝수
        count=N//5
        count+=(N%5)//2
    elif (N%5)%2==1: #5로 나눈 나머지가 홀수
        count=(N//5)-1
        if count==0:
            count=N//2 #6인 경우
        else:
            count+=(N-5*count)//2

print(count)


##다른 풀이 > so 간단..
#while n>0:
#    if n%5==0:
#        count+=n//5
#        break
    
#    n-=2
#    count+=1
#if n<0:
#    print(-1)
#else:
#    print(count)
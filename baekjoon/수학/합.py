import sys

read=sys.stdin.readline
count=int(read())
sum=0

for i in range(count+1):
    sum+=i
print(sum)


# sum 함수 이용하여 한줄로 작성하는 법
print(sum(range(1, int(input())+1)))

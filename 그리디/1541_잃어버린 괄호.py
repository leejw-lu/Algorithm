import sys
read=sys.stdin.readline

#55-50+40
a=read().split('-') #a는 배열 ['55', '50+40']
num=[]
sum=0

for i in a:
    count=0
    s=i.split('+') #[50,40]
    for j in s:
        count+=int(j)   #not = yes +=
    num.append(count)
sum=num[0]          #not += yes =

for i in range(1, len(num)):
    sum-=num[i]

print(sum)

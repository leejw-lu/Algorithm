import sys
read=sys.stdin.readline

num = int(read())
line=0
sum=0

while num>sum:
    line+=1
    sum+=line

dif=sum-num #해당line의 마지막 인덱스에서 얼만큼 떨어져 있는지

if line%2: #홀수층
    top=dif+1
    down=line-dif
else: #짝수층
    top=line-dif
    down=dif+1

print(f'{top}/{down}')




            
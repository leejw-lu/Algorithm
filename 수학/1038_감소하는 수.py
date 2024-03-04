from itertools import combinations
n=int(input())
result=[]

#9876543210 감소하는 수
for i in range(1,11):
    for j in combinations(range(10), i): #0~9로 조합 만들기
        num=sorted(list(j), reverse=True)
        result.append(int(''.join(map(str,num))))

result.sort() #감소하는 수 정렬

if n>=len(result):
    print(-1)
else:
    print(result[n])
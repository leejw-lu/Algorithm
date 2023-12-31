import sys
a,b=map(str,sys.stdin.readline().rstrip().split())
result=[]

for i in range(len(b)-len(a)+1): #길이 같게 (B 시작점 지정)
    count=0
    for j in range(len(a)):
        if a[j] != b[i+j]: #a 기준으로 b 끝까지 검사
            count+=1
    result.append(count)

print(min(result))


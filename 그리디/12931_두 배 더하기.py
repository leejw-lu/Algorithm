n=int(input())
arr=list(map(int,input().split()))
arr.sort()

result=0
#arr배열 (B)에서 A배열 (모든 행 0) 로 만들기 (A->B보다 B->A가 최소 개수)

while True:
    for i in range(n):
        if arr[i] % 2: # 홀수-> 짝수 만들기
            arr[i] -= 1
            result += 1
    if sum(arr) == 0:
        break
    for i in range(n): # 짝수
        arr[i] /= 2
    result += 1
print(result)
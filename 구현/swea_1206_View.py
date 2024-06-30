T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    building=list(map(int,input().split()))
    count=0
    for i in range(2,n-2):
        left=max(building[i-1], building[i-2])
        right=max(building[i+1], building[i+2])
        best = max(left, right)
        if building[i] > best:
            count += (building[i] - best)
    print(f'#{test_case} {count}')
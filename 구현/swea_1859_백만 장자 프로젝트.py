T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n=int(input())
    arr=list(map(int,input().split()))
    profit=0

    #거꾸로 계산하기
    maxValue=arr[-1]
    for i in range(n-2,-1,-1):
        if maxValue>arr[i]:
            profit+=maxValue-arr[i]
        else:
            maxValue=arr[i]
    print(f'#{test_case} {profit}')
def solution(N, number):
    answer=-1
    
    dp=[set([int(str(N)*i)]) for i in range(1,9)] #{N}, {NN}, {NNN}
    for i in range(8): #N을 i번 사용
        for j in range(i): #j개
            for num1 in dp[j]:
                #i-j개
                for num2 in dp[i-j-1]:
                    dp[i].add(num1+num2)
                    dp[i].add(num1-num2)
                    dp[i].add(num1*num2)
                    if num2 !=0:
                        dp[i].add(num1//num2)
        #number가 값에 있으면 반환
        if number in dp[i]:
            return i+1

    return answer
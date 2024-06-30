def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j==0: #가장 왼쪽
                triangle[i][0]+=triangle[i-1][0]
            elif j==i: #가장 오른쪽
                triangle[i][j]+=triangle[i-1][j-1]
            else: #가운데
                triangle[i][j]+=max(triangle[i-1][j], triangle[i-1][j-1])
                
    return max(triangle[-1])
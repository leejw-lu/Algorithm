#완전탐색
n=int(input())
arr=[list(input()) for _ in range(n)]

def checkColorNum(): #가장 긴 연속부분 (행or열) 개수 return
    maxCnt=1
    for i in range(n):
        #가로
        tmp=1
        for j in range(1,n):
            if arr[i][j]==arr[i][j-1]: #이전 것과 같다면.
                tmp+=1
            else:    
                tmp=1   #이전과 다르다면 1로 초기화.
            maxCnt=max(maxCnt,tmp)

        #세로
        tmp=1
        for j in range(1,n):
            if arr[j][i]==arr[j-1][i]:
                tmp+=1
            else:
                tmp=1
            maxCnt=max(maxCnt,tmp)
    
    return maxCnt

#색깔 다른 부분 swap (오른쪽 & 아래쪽만 해도 O)
result=1
for i in range(n):
    for j in range(n-1):
        #오른쪽 swap
        if j+1<n and arr[i][j]!=arr[i][j+1]:
            arr[i][j], arr[i][j+1]= arr[i][j+1], arr[i][j] #swap
            result=max(result, checkColorNum()) #최대 개수 count
            arr[i][j], arr[i][j+1]= arr[i][j+1], arr[i][j] #원래대로 되돌리기

        #아래쪽 swap
        if i+1<n and arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j]= arr[i+1][j], arr[i][j] #swap
            result=max(result,checkColorNum())
            arr[i][j], arr[i+1][j]= arr[i+1][j], arr[i][j] #원래대로 되돌리기

print(result)
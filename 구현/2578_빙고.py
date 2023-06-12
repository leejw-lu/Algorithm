import sys
read=sys.stdin.readline

#함수1: 빙고 줄 개수 return
def bingo_count():
    global bingo
    b_count=0

    # 가로 확인
    for i in bingo: 
        if i.count(-1) == 5:
            b_count += 1
    
    # 세로 확인 (굳이 zip 안써도 될거 같은..)
    zip_bingo = list(map(list, zip(*bingo)))
    for i in zip_bingo: 
      if i.count(-1) == 5:
           b_count += 1

    #대각선
    count=0; count2=0
    for i in range(5):
        #\ 대각선 (i==j)
        if bingo[i][i]==-1: 
            count+=1
        #/ 대각선 (i+j=4)
        if bingo[i][4-i]==-1: 
            count2+=1

    if count==5:
        b_count+=1
    if count2==5:
        b_count+=1


    return b_count

#함수2: mc가 부른 search수가 bingo에 있는지 확인 후 있으면 -1로 바꾸기 
#(원래 INF하려했는데 python int형에선 X)
def number_check(n):
    global bingo
    for i in range(5):
         for j in range(5):
              if n==bingo[i][j]:
                   bingo[i][j]=-1 #변경
                   break

#입력
bingo=[list(map(int,read().split())) for _ in range(5)]
mc=[]
for _ in range(5):
    mc+=list(map(int, input().split()))

## main
for i in range(25):
    search=mc[i] #mc가 부른 숫자
    number_check(search) 

    #if i>=12: #최소 12번 이후 정답 가능 >>>> 이거 조건 넣으면 실패뜨네..
    result= bingo_count()
    if result >= 3:     #==3이 아닌 >=3을 해줘야 한다.
        print(i+1)
        break

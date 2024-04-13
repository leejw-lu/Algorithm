t=int(input())
for tc in range(t):
    n,k=map(int,input().split())
    data=list(input())
    turn=n//4
    result=0
    box=[]
    for _ in range(turn):
        for i in range(0,n,turn):
            tmp=int(''.join(data[i:i+turn]), 16)
            if tmp not in box:
                box.append(tmp)
        data=[data[-1]]+data[:-1]

    print("#{} {}".format(tc + 1, sorted(box, reverse=True)[k - 1]))
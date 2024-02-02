n=int(input())
cranes=list(map(int,input().split())) #동시에 움직임
m=int(input())
boxes=list(map(int,input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
result=0

if cranes[0]<boxes[0]:
    print(-1)
    exit(0)

while boxes:
    for c in cranes:
        if boxes and c<boxes[-1]: #현재 크레인보다 box가 더 무거운 경우
            continue
        for b in boxes:
            if c>=b:
                boxes.remove(b)
                break
    result+=1

print(result)
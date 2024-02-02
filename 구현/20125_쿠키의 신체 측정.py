n=int(input())
graph=[list(input()) for _ in range(n)]
heartX,hearY=0,0
waistX=0

#심장 위치 구하기
def heart():
    global heartX,heartY
    for i in range(n):
        for j in range(n):
            if graph[i][j]=='*':
                heartX,heartY= i+1,j #머리 바로 아래
                return
            
#왼팔:
def left_arm():
    count=0
    for i in range(heartY-1,-1,-1): #0번 idx가 *일 수 있으니 -1까지 조사하기
        if graph[heartX][i]!='*':
            break
        else:
            count+=1
    return count

#오른팔:
def right_arm():
    count=0
    for i in range(heartY+1,n):
        if graph[heartX][i]!='*':
            break
        else:
            count+=1
    return count

#허리:
def waist():
    count=0
    global waistX
    for i in range(heartX+1,n):
        if graph[i][heartY]!='*':
            waistX=i
            break
        else:
            count+=1
    return count

#왼다리
def left_leg():
    count=0
    for i in range(waistX,n):
        if graph[i][heartY-1]!='*':
            break
        else:
            count+=1
    return count

#오른다리
def right_leg():
    count=0
    for i in range(waistX,n):
        if graph[i][heartY+1]!='*':
            break
        else:
            count+=1
    return count


#심장위치 print
heart()
print(heartX+1, heartY+1)

#왼팔, 오른팔, 허리, 왼다리, 오른다리 길이
print(left_arm(),right_arm(),waist(),left_leg(),right_leg())
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

#방향별 모래 비율 위치
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]

s_x, s_y = n//2, n//2  # 시작좌표(x좌표)
ans = 0  # out_sand

# 모래 계산하는 함수

def move(time, dx, dy, direction):
    global ans, s_x, s_y

    # y좌표 계산 & x좌표 갱신
    for _ in range(time):
        s_x += dx
        s_y += dy
        if s_x < 0 or s_y < 0:  # 범위 밖이면 stop
            break

        #a, out_sand
        total = 0  # a 구하기 위한 변수
        for dx, dy, z in direction:
            nx = s_x + dx
            ny = s_y + dy
            if z == 0:  # a(나머지)
                new_sand = graph[s_x][s_y] - total
            else:  # 비율
                new_sand = int(graph[s_x][s_y] * z)
                total += new_sand

            if 0 <= nx < n and 0 <= ny < n:   # 인덱스 범위 이면 값 갱신
                graph[nx][ny] += new_sand
            else:  # 범위 밖이면 ans 카운트
                ans += new_sand

#토네이도 회전 방향(y위치)
for i in range(1,n+1):
    if i % 2:
        move(i, 0, -1, left)
        move(i, 1, 0, down)
    else:
        move(i, 0, 1, right)
        move(i, -1, 0, up)

print(ans)
from collections import deque

n, m, p, C, d = map(int, input().split())
Sx, Sy = map(int, input().split())
rx, ry = Sx - 1, Sy - 1
S = []
graph = [[0] * n for _ in range(n)]
graph[rx][ry] = -1
stun_santa = [0] * (p + 1)
alive_santa = [1] * (p + 1)
alive_santa[0] = 0
score = [0] * (p + 1)

for _ in range(p):
    a, b, c = map(int, input().split())
    a, b, c = a, b - 1, c - 1
    S.append((a, b, c))
    graph[b][c] = a


# 루돌프와 가장 가까운 산타 찾기
def rudolf_most_near(x, y):
    Q = deque()
    Q.append((x, y))
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    visit = [[0] * n for _ in range(n)]
    visit[x][y] = 1
    distance = [[0] * n for _ in range(n)]
    temp = []
    sx, sy = x, y
    while Q:
        x, y = Q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                distance[nx][ny] = distance[x][y] + 1
                if graph[nx][ny] == 0:
                    Q.append((nx, ny))
                if graph[nx][ny] > 0:
                    temp.append((nx, ny, abs(sx - nx) ** 2 + abs(sy - ny) ** 2))

    return sorted(temp, key=lambda x: (-x[2], x[0], x[1]))


# 루돌프 움직이기
def rudolf_move(x, y, ex, ey):
    Q = deque()
    Q.append((x, y))
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    visit = [[0] * n for _ in range(n)]
    visit[x][y] = 1
    distance = [[0] * n for _ in range(n)]
    temp = []
    sx, sy = x, y
    while Q:
        x, y = Q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                temp.append((nx, ny, abs(nx - ex) ** 2 + abs(ny - ey) ** 2, dx[i], dy[i]))

    return sorted(temp, key=lambda x: (-x[2], x[0], x[1]))


# 산타 움직이기
def santa_move(number, x, y, ex, ey):
    Q = deque()
    Q.append((x, y))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    distance = abs(x - ex) ** 2 + abs(y - ey) ** 2
    temp = []
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dist = abs(nx - ex) ** 2 + abs(ny - ey) ** 2
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= 0 and dist < distance:
                distance = dist
                temp.append((nx, ny, abs(ex - nx) ** 2 + abs(ey - ny) ** 2, dx[i], dy[i]))

    return sorted(temp, key=lambda x: (-x[2]))


# 산타가 움직여서 루돌프랑 충돌
def santa_hit_rudolf(number, x, y, dx, dy):
    nx = x + (dx * d)
    ny = y + (dy * d)
    if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 0:
            graph[nx][ny] = number
        elif graph[nx][ny] > 0:

            santa_hit_santa(nx, ny, dx, dy, graph[nx][ny])

            graph[nx][ny] = number
        return
    else:

        alive_santa[number] = 0
        return


# 산타가 날아가는데 산타랑 충돌
def santa_hit_santa(x, y, dx, dy, post_value):
    Q = deque()
    Q.append((x, y, post_value))
    while Q:
        x, y, value = Q.popleft()
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = value

            else:
                Q.append((nx, ny, graph[nx][ny]))
                graph[nx][ny] = value

        else:
            alive_santa[value] = 0


# 루돌프가 움직여서 충돌
def rudolf_hit(x, y, dx, dy, number):
    nx = x + dx * C
    ny = y + dy * C
    if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
        else:
            santa_hit_santa(nx, ny, dx, dy, graph[nx][ny])
            graph[nx][ny] = graph[x][y]
    else:
        alive_santa[number] = 0


time = 0
for T in range(m):
    if sum(alive_santa) == 0:
        break

    time += 1

    # 루돌프 위치 찾기
    most_near_santa = rudolf_most_near(rx, ry)

    ex, ey, dist = most_near_santa.pop()
    graph[rx][ry] = 0
    # 루돌프 움직이기
    rudolf_movement = rudolf_move(rx, ry, ex, ey)
    rx, ry, rdist, dx, dy = rudolf_movement.pop()
    # 만약 루돌프가 산타와 부딪히면
    if graph[rx][ry] > 0:
        stun_santa[graph[rx][ry]] = 2
        score[graph[rx][ry]] += C
        rudolf_hit(rx, ry, dx, dy, graph[rx][ry])

    graph[rx][ry] = -1

    S = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                S.append((graph[i][j], i, j))
    S.sort(key=lambda x: x[0])

    for z in range(1, p + 1):
        santax, santay = -1, -1
        for i in range(n):
            for j in range(n):
                if graph[i][j] == z:
                    santax, santay = i, j
        # 만약 해당 루돌프가 존재하지 않으면
        if santax == -1 and santay == -1:
            continue
        number = graph[santax][santay]
        if stun_santa[number] != 0:
            continue

        santa_movement = santa_move(number, santax, santay, rx, ry)
        if len(santa_movement) == 0:
            continue

        graph[santax][santay] = 0
        sx, sy, dist, dx, dy = santa_movement.pop()
        if graph[sx][sy] == 0:
            graph[sx][sy] = number

        elif graph[sx][sy] == -1:
            score[number] += d
            stun_santa[number] = 2

            santa_hit_rudolf(number, sx, sy, -dx, -dy)

    for i in range(1, p + 1):
        if alive_santa[i] == 1:
            score[i] += 1
    for i in range(1, p + 1):
        if stun_santa[i] > 0:
            stun_santa[i] -= 1

print(*score[1:])
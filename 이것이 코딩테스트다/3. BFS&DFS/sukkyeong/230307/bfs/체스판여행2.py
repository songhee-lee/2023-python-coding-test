import collections

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [[[[-1, -1]] * 3 for _ in range(n * n + 1)] for _ in range(n)] for _ in range(n)]
dx1 = [-2, -1, 1, 2, 2, 1, -1, -2]
dy1 = [1, 2, 2, 1, -1, -2, -2, -1]  # 나이트
dx2 = [0, 0, 1, -1]
dy2 = [1, -1, 0, 0]  # 룩
dx3 = [1, 1, -1, -1]
dy3 = [1, -1, 1, -1]  # 비숍

q = collections.deque()
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            for k in range(3):
                visited[i][j][1][k] = [0, 0]
                q.append([i, j, 1, k])
            break

ans = ([-1, -1])
while q:
    x, y, num, cur = q.popleft()
    p = visited[x][y][num][cur]
    if num == n * n:
        # [a, b] > [c, d]
        # x[0] 비교, 같으면 x[1] 비교
        if ans == [-1, -1] or ans > p:
            ans = p

    for i in range(3):
        if cur != i:
            np = [p[0] + 1, p[1] + 1]
            if visited[x][y][num][i] == [-1, -1] or visited[x][y][num][i] > np:
                visited[x][y][num][i] = np
                q.append([x, y, num, i])

    np = [p[0] + 1, p[1]]
    if cur == 0:
        for i in range(8):
            nx = x + dx1[i]
            ny = y + dy1[i]
            if 0 <= nx < n and 0 <= ny < n:
                nxt = num
                if maps[nx][ny] == num + 1:
                    nxt += 1

                if visited[nx][ny][nxt][cur] == [-1, -1] or visited[nx][ny][nxt][cur] > np:
                    visited[nx][ny][nxt][cur] = np
                    q.append([nx, ny, nxt, cur])

    if cur == 1:
        for i in range(4):
            k = 1
            while True:
                nx = x + dx2[i] * k
                ny = y + dy2[i] * k

                if 0 <= nx < n and 0 <= ny < n:
                    nxt = num
                    if maps[nx][ny] == num + 1:
                        nxt += 1

                    if visited[nx][ny][nxt][cur] == [-1, -1] or visited[nx][ny][nxt][cur] > np:
                        visited[nx][ny][nxt][cur] = np
                        q.append([nx, ny, nxt, cur])
                else:
                    break
                k += 1

    if cur == 2:
        for i in range(4):
            k = 1
            while True:
                nx = x + dx3[i] * k
                ny = y + dy3[i] * k

                if 0 <= nx < n and 0 <= ny < n:
                    nxt = num
                    if maps[nx][ny] == num + 1:
                        nxt += 1
                    if visited[nx][ny][nxt][cur] == [-1, -1] or visited[nx][ny][nxt][cur] > np:
                        visited[nx][ny][nxt][cur] = np
                        q.append([nx, ny, nxt, cur])
                else:
                    break
                k += 1

print(*ans)

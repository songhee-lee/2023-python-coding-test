import collections
import math

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[[[-1] * 3 for _ in range(n * n + 1)]
            for _ in range(n)] for _ in range(n)]
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
                visited[i][j][1][k] = 0
                q.append([i, j, 1, k])
            break

ans = -1
while q:
    x, y, num, cur = q.popleft()
    if num == n * n:
        ans = visited[x][y][num][cur]
        break

    for i in range(3):
        if cur == i:
            continue
        if visited[x][y][num][i] == -1:
            visited[x][y][num][i] = visited[x][y][num][cur] + 1
            q.append((x, y, num, i))

    if cur == 0:
        for k in range(8):
            nx = x + dx1[k]
            ny = y + dy1[k]
            if 0 <= nx < n and 0 <= ny < n:
                nxt = num
                if maps[nx][ny] == num + 1:
                    nxt = num + 1
                if visited[nx][ny][nxt][cur] == -1:
                    visited[nx][ny][nxt][cur] = visited[x][y][num][cur] + 1
                    q.append([nx, ny, nxt, cur])
    elif cur == 1:
        for k in range(4):
            l = 1
            while True:
                nx = x + dx2[k] * l
                ny = y + dy2[k] * l
                if 0 <= nx < n and 0 <= ny < n:
                    nxt = num
                    if maps[nx][ny] == num + 1:
                        nxt = num + 1
                    if visited[nx][ny][nxt][cur] == -1:
                        visited[nx][ny][nxt][cur] = visited[x][y][num][cur] + 1
                        q.append([nx, ny, nxt, cur])
                else:
                    break
                l += 1
    else:
        for k in range(4):
            l = 1
            while True:
                nx = x + dx3[k] * l
                ny = y + dy3[k] * l
                if 0 <= nx < n and 0 <= ny < n:
                    nxt = num
                    if maps[nx][ny] == num + 1:
                        nxt = num + 1
                    if visited[nx][ny][nxt][cur] == -1:
                        visited[nx][ny][nxt][cur] = visited[x][y][num][cur] + 1
                        q.append([nx, ny, nxt, cur])
                else:
                    break
                l += 1

print(ans)

"""

- 빨간 구슬만 구멍에 빠뜨리기
- 기울이기 : 상하좌우
"""

from collections import deque

def move(x, y, dx, dy):
    m = 0   # 움직인 횟수
    while True:
        if maps[x][y] == 'O':   # 구멍이면 stop
            break
        if maps[x][y] == '#':   # 벽 만나면 이전으로 돌아가서 stop
            x -= dx
            y -= dy
            break
        x += dx
        y += dy
        m += 1
    return x, y, m 


# 1. 입력 받기
N, M = map(int, input().split())    # 세로, 가로 크기

maps = []
for i in range(N):
    line = list(input())
    for j in range(M):
        if line[j] == 'B':      # 파란 구슬
            bx, by = i, j
            line[j] ='.'
        elif line[j] == 'R':    # 빨간 구슬
            rx, ry = i, j
            line[j] = '.'
        elif line[j] == 'O':    # 구멍
            hole = (i, j)
    maps.append(line)

# 상하좌우 이동
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# BFS 
q = deque([(1, rx, ry, bx, by)])    # 움직임 횟수, Red, Blue 좌표
visited = set([(rx, ry, bx, by)])   # 방문한 Red, Blue 좌표 기록

answer = 1e9
while q:
    count, rx, ry, bx, by = q.popleft()

    for i in range(4):
        nrx, nry, mr = move(rx, ry, dx[i], dy[i])
        nbx, nby, mb = move(bx, by, dx[i], dy[i])

        if maps[nbx][nby] == 'O':   # blue 가 구멍에 빠지면 안됨
            continue
        if maps[nrx][nry] == 'O':   # Red가 구멍에 빠지면 최소 횟수 기록
            answer = min(answer, count)
        
        # RED / BLUE 충돌한 경우
        if nrx == nbx and nry == nby :
            # 더 많이 움직인 쪽이 뒤에 있는 것이므로 back 시키기
            if mr < mb : nbx, nby = nbx-dx[i], nby-dy[i]
            else: nrx, nry = nrx-dx[i], nry-dy[i]

        # 방문하지 않은 좌표 조합이면 큐에 추가
        if (nrx, nry, nbx, nby) not in visited :
            visited.add((nrx, nry, nbx, nby))
            q.append((count+1, nrx, nry, nbx, nby))

if answer == 1e9:
    answer = -1
print(answer)
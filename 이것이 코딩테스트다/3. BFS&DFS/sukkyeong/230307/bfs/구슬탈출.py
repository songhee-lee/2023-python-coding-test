'''
1. 빨간 구슬과 파란 구슬의 위치를 (rx, ry), (bx, by)에 저장한다

2. 큐에 두 구슬의 좌표를 [rx, ry, bx, by] 형태로 입력하고 방문을 체크한다

3. bfs로 이동할 때 현재 방향에서 두 구슬을 갈 수 있는 만큼 이동시킨다

   중간에 구멍에 빠지거나 벽을 만나면 break 한다

4. 파란 구슬이 구멍에 빠지면 continue해서 예외처리한다

   빨간 구슬이 빠지면 기울인 횟수 cnt를 출력하고 bfs를 끝낸다

5. 빨간구슬과 파란구슬이 같은 위치에 놓이면 두 구슬의 이동 거리를 비교하여 겹치지 않게 처리한다

6. 두 구슬의 위치가 방문한 적 없는 위치이면 c에 기록하고 큐에 입력한다

7. 큐가 비어있을 때까지 구멍에 빠지지 않으면 -1을 출력하고 끝낸다
'''
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    cnt = 1
    while q:
        qlen = len(q)
        for _ in range(qlen):
            rx, ry, bx, by = q.popleft()
            for i in range(4):
                nrx, nry, nbx, nby = rx, ry, bx, by
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if a[nrx][nry] == 'O':
                        break
                    if a[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break

                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if a[nbx][nby] == 'O':
                        break
                    if a[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break

                if a[nbx][nby] == 'O':
                    continue
                if a[nrx][nry] == 'O':
                    print(cnt)
                    return

                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not c[nrx][nry][nbx][nby]:
                    c[nrx][nry][nbx][nby] = 1
                    q.append([nrx, nry, nbx, nby])

        cnt += 1
    print(-1)
    return


n, m = map(int, input().split())

a = []
for i in range(n):
    row = list(input().strip())
    a.append(row)
    for j in range(m):
        if a[i][j] == 'B':
            bx, by = i, j
            a[i][j] = '.'
        elif a[i][j] == 'R':
            rx, ry = i, j
            a[i][j] = '.'

q = deque()
c = [[[[0 for _ in range(m)] for _ in range(n)]
      for _ in range(m)] for _ in range(n)]
q.append([rx, ry, bx, by])
c[rx][ry][bx][by] = 1
bfs()

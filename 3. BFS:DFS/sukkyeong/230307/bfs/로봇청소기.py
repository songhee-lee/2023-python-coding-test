from sys import stdin
from collections import deque

input = stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[0]*2**10 for _ in range(20)] for _ in range(20)]
visited_num = 0
w = h = 0


def solv():
    global w, h
    while True:
        w, h = map(int, input().split())
        if w == h == 0:
            return

        board = []
        sx = sy = -1
        trash_idx = 0
        target_bitmask = 0
        for x in range(h):
            board.append(list(input().strip()))
            for y in range(w):
                if board[x][y] == 'o':
                    sx, sy = x, y
                    board[x][y] = '.'
                elif board[x][y] == '*':
                    target_bitmask |= (1 << trash_idx)
                    board[x][y] = str(trash_idx)
                    trash_idx += 1

        print(bfs(sx, sy, board, target_bitmask))


def bfs(sx, sy, board, target_bitmask):
    global visited, visited_num
    visited_num += 1
    visited[sx][sy][0] = True

    q = deque([(sx, sy, 0, 0)])

    while q:
        x, y, cnt, bitmask = q.pop()
        if bitmask == target_bitmask:
            return cnt

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if boundray_validator(nx, ny, board):
                if board[nx][ny].isdigit():
                    trash_idx = int(board[nx][ny])
                    nxt_bitmask = bitmask | (1 << trash_idx)
                    if visited[nx][ny][nxt_bitmask] != visited_num:
                        visited[nx][ny][nxt_bitmask] = visited_num
                        q.appendleft((nx, ny, cnt+1, nxt_bitmask))
                else:
                    if visited[nx][ny][bitmask] != visited_num:
                        visited[nx][ny][bitmask] = visited_num
                        q.appendleft((nx, ny, cnt+1, bitmask))

    return -1


def boundray_validator(x, y, board):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    elif board[x][y] == 'x':
        return False
    return True


solv()

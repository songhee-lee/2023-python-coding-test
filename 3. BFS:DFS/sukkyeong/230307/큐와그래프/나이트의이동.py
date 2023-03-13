''''''
from collections import deque
import sys
input = sys.stdin.readline

t = int(input().rstrip())


def bfs():
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    q = deque()
    q.append((startX, startY))
    while q:
        x, y = q.popleft()
        if x == endX and y == endY:
            return matrix[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx, ny))


for _ in range(t):
    l = int(input().rstrip())
    startX, startY = map(int, input().rstrip().split())
    endX, endY = map(int, input().rstrip().split())
    matrix = [[0]*l for _ in range(l)]
    matrix[startX][startY] = 1
    print(bfs())

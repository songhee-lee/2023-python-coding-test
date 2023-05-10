""" 
- 1초 / 256MB

- 나이트를 몇 번 움직여야 원하는 칸에 이동할 수 있을까
"""
from collections import deque

T = int(input())    # 테스트 케이스 개수

# 나이트 이동 가능한 경로
dx = (-2, -2, -1, 1, 2, 2, 1, -1)
dy = (-1, 1, 2, 2, 1, -1, -2, -2)

def bfs(start, goal):
    q = deque([start])
    visited[start[0]][start[1]] = 1

    while q:
        x, y = q.popleft()

        if x == goal[0] and y == goal[1]:
            return visited[x][y] -1

        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

for _ in range(T):
    N = int(input())    # 체스판 길이
    now = tuple(map(int, input().split()))  # 현재 칸
    want = tuple(map(int, input().split())) # 이동하고 싶은 칸
    
    visited = [ [0] *N for _ in range(N) ]    # 방문한 칸 표시
    print(bfs(now, want))
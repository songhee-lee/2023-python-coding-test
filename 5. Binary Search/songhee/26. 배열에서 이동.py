""" 
- (1,1)에서 상하좌우 이동으로 (N,N)까지 이동
- 이동하기 위해 거쳐간 수 중 최댓값과 최솟값의 차이가 가장 작아지는 경우
"""
from collections import deque
import sys
input = sys.stdin.readline

# left ~ right 숫자 사이로 (N,N)까지 이동 가능한지 확인하는 함수
def bfs(left, right):
    visited = [[False] * N for _ in range(N)]
    visited[0][0] = True

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()

        if x == N-1 and y == N-1:
            return True

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if left <= maps[nx][ny] <= right:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    
    return False

N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))


# 이진탐색
## 리스트 최솟값 <= left <= (출발지와 도착지 중 작은값)
## (출발지와 도착지 중 큰 값) <= right <= 리스트 최댓값 
l_min, r_max = min(map(min, maps)), max(map(max, maps))
l_max = min(maps[0][0], maps[N-1][N-1])
r_min = max(maps[0][0], maps[N-1][N-1])

left, right = l_min, r_min
ans = 1e9
while l_min <= left <= l_max and r_min <= right <= r_max:
    if bfs(left, right):
        ans = min(ans, right-left)
        left += 1
    else:
        right += 1

print(ans)
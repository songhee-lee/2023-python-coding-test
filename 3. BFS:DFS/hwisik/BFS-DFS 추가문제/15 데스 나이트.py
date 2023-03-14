'''
- 데스 나이트의 최소 이동 횟수 구하기 -> ✅'BFS'
- 이동 횟수 배열이 방문 표시 배열의 역할을 한다.
    - dist[i][j] == -1 : 방문한 적 없음
    - dist[i][j] != -1 : 방문했음
'''
from collections import deque
import sys

# BFS
def bfs():
    queue = deque([(r1, c1)]) # 데스 나이트의 초기 위치
    dist[r1][c1] = 0 # 데스 나이트의 초기 위치의 이동 횟수 = 0
    
    while queue:
        x, y = queue.popleft()
        
        # 도착했다면 종료
        if x == r2 and y == c2: 
            return
        
        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            
            # 방문한 적 없으면
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1 # 이동 횟수 갱신
                queue.append((nx, ny))

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dist = [[-1] * n for _ in range(n)]

# 데스 나이트의 방향 정보
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

# BFS 수행
bfs()

# 도착지에 이동할 수 없는 경우 처리
ret = -1 if dist[r2][c2] == -1 else dist[r2][c2]

# 출력
print(ret)
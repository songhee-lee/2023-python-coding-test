'''
- n : 세로(열), m : 가로(행)
- '1111' XOR 'graph[i][j]' -> 벽이 없는 곳은 0으로 나온다.
    - 
'''
from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    room_count = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if i == 0:
                    if 1 & graph[x][y]: continue
                elif i == 1:
                    if 2 & graph[x][y]: continue
                elif i == 2:
                    if 4 & graph[x][y]: continue
                elif i == 3:
                    if 8 & graph[x][y]: continue
                
                visited[nx][ny] = 1
                queue.append((nx, ny))
                room_count += 1
                
    return room_count

n, m = map(int, input().split())

graph = []
visited = [[0] * n for _ in range(m)]

# 방향 정보(남, 동, 북, 서)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for _ in range(m):
    input_data = list(map(int, input().split()))
    graph.append(input_data)

total_room_count = 0
max_room_size = 0
max_room_size_when_removed_wall = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            max_room_size = max(max_room_size, bfs(i, j))
            total_room_count += 1

for i in range(m):
    for j in range(n):
        remove_wall_dir = 1
        while remove_wall_dir < 9:
            if remove_wall_dir & graph[i][j]:
                visited = [[0] * n for _ in range(m)]
                graph[i][j] -= remove_wall_dir
                max_room_size_when_removed_wall = max(max_room_size_when_removed_wall, bfs(i, j))
                graph[i][j] += remove_wall_dir
            remove_wall_dir *= 2

print(total_room_count)
print(max_room_size)
print(max_room_size_when_removed_wall)
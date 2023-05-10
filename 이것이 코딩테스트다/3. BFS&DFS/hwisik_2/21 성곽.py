'''
- 벽 -> 1 : 서쪽, 2 : 북쪽, 4 : 동쪽, 8 : 남쪽
- 모든 방향에 벽이 있으면, (1 + 2 + 4 + 8 => 15) == (1 & 2 & 4 & 8 => 15)
- 벽이 있는지 없는지 확인하는 방법 -> AND 연산

아이디어 - (1), (2)
- 방문하지 않은 모든 노드에 대해서, BFS를 수행한다.
- 현재 노드에 벽이 있는지 확인하며, 문제의 조건에 맞다면 연결된 모든 다음 노드를 큐에 추가한다.

아이디어 - (3)
- (1), (2) 에서 벽이 있는지 확인하는 방법 그대로, 벽을 제거할 때 사용한다.
- 모든 방향에 대해서 벽을 제거해보면서, 최대로 만들 수 있는 방의 크기를 구한다.

-> ✅'다시풀기'
'''
from collections import deque

# BFS
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    room_count = 1 # 방의 개수
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                
                # 벽이 있는지 확인
                if i == 0:
                    if 1 & graph[x][y]: continue # 서쪽
                elif i == 1:
                    if 2 & graph[x][y]: continue # 북쪽
                elif i == 2:
                    if 4 & graph[x][y]: continue # 동쪽
                elif i == 3:
                    if 8 & graph[x][y]: continue # 남쪽
                
                visited[nx][ny] = 1
                queue.append((nx, ny))
                room_count += 1 # 방의 개수 + 1
                
    return room_count

n, m = map(int, input().split())

graph = []
visited = [[0] * n for _ in range(m)]

# 방향 정보(서, 북, 동, 남)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for _ in range(m):
    input_data = list(map(int, input().split()))
    graph.append(input_data)

total_room_count = 0 # 1. 이 성에 있는 방의 개수
max_room_size = 0 # 2. 가장 넓은 방의 넓이
max_room_size_when_removed_wall = 0 # 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기

# 각 방에 대해서 BFS 수행
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            max_room_size = max(max_room_size, bfs(i, j))
            total_room_count += 1

# 하나의 벽을 제거했을 때
for i in range(m):
    for j in range(n):
        remove_wall_dir = 1 # 시작은 서쪽 확인
        while remove_wall_dir < 9:
            if remove_wall_dir & graph[i][j]: # 벽 있는지 확인
                visited = [[0] * n for _ in range(m)]
                
                graph[i][j] -= remove_wall_dir # 벽 제거
                
                # 벽 제거했을 때 BFS
                max_room_size_when_removed_wall = max(max_room_size_when_removed_wall, bfs(i, j))
                
                graph[i][j] += remove_wall_dir # 다음을 위해 벽 재건
                
            # 1 : 서, 2 : 북, 4 : 동, 8 : 남
            remove_wall_dir *= 2

# 출력
print(total_room_count)
print(max_room_size)
print(max_room_size_when_removed_wall)
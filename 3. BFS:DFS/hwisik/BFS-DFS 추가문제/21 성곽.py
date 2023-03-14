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

def get_room_area(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    room_area = 1
    
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
                room_area += 1
                
    return room_area
            
n, m = map(int, input().split())

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

# 방향 정보(서, 북, 동, 남)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 이 성에 있는 방의 개수
# 가장 넓은 방의 넓이
# 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
room_count = 0
max_room_area = 0
max_room_area_when_removed_wall = 0

visited = [[0] * n for _ in range(m)]

# 이 성에 있는 방의 개수와 가장 넓은 방의 넓이를 구한다.
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            max_room_area = max(max_room_area, get_room_area(i, j))
            room_count += 1

# 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기를 구한다.
for i in range(m):
    for j in range(n):
        wall_dir = 1
        while wall_dir < 9:
            if wall_dir & graph[i][j]:
                visited = [[0] * n for _ in range(m)]
                graph[i][j] -= wall_dir
                max_room_area_when_removed_wall = max(max_room_area_when_removed_wall,get_room_area(i, j))
                graph[i][j] += wall_dir
            wall_dir *= 2
                
print(room_count)
print(max_room_area)
print(max_room_area_when_removed_wall)
'''
- 현재 상어의 위치와, 상어의 크기를 가지고 아기 상어의 크기보다 작은 모든 물고기의 위치를 구한다.
- 위에서 구한 물고기의 위치를 토대로, 먹을 수 있는 물고기들 중 최단 거리에 위치한 물고기의 위치를 구한다.
- BFS를 사용해서현재 상어의 위치에서 해당 물고기의 위치까지 갈 수 있다면, 배열에 저장한다.
- BFS가 끝나면 '먹을 수 있는 물고기들의 위치' 배열을 반환한다.
- 해당 배열의 맨 앞 물고기의 위치를 꺼내서,
    - 물고기 먹은 횟수와 물고기를 잡아먹는데 걸린 시간을 갱신.
    - 먹힌 물고기의 위치와 원래 상어의 위치의 값을 0으로 갱신.
    - 현재 상어의 위치를 먹힌 물고기의 위치로 갱신.
- 아기 상어 자신의 크기와 같은 수의 물고기를 먹었다면, 상어의 크기 + 1
'''
from collections import deque
import sys
            
# 아기 상어 크기보다 작은 물고기의 위치 집합 반환
def find_smaller_fish(shark_size):
    smaller_fish = set()
    
    for i in range(n):
        for j in range(n):
            if 1 <= graph[i][j] <= 6 and graph[i][j] < shark_size:
                smaller_fish.add((i, j))
    
    return smaller_fish

# 먹을 수 있는 물고기들 중 최단 거리 찾기 (BFS)
def find_short_dist(x, y, shark_size):
    dist = [[-1] * n for _ in range(n)] # 물고기까지의 거리 배열
    queue = deque([(x, y)])
    ret = [] # 먹을 수 있는 물고기 저장하는 배열
    smaller_fish = find_smaller_fish(shark_size) # 상어 크기보다 작은 물고기들의 위치 집합
    
    dist[x][y] = 0 # 최단 거리 저장을 위해
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if graph[nx][ny] > shark_size: continue
            
            # 방문하지 않았고, 먹을 수 있거나 상어와 크기가 같다면
            if graph[nx][ny] <= shark_size and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1 # 최단 거리 갱신
                queue.append((nx, ny))
                
                # 먹을 수 있는 물고기의 위치에 도달했다면(상어의 크기보다 작은 물고기라면)
                if (nx, ny) in smaller_fish:
                    ret.append((nx, ny, dist[nx][ny]))
                
    # 먹을 수 있는 물고기가 1마리 보다 많다면, '거리가 가장 가까운 물고기',
    # 거리가 가까운 물고기가 많다면, '가장 위에 있는 물고기'(X : 오름차순),
    # 그러한 물고기가 여러마리라면, '가장 왼쪽에 있는 물고기'(Y : 오름차순),
    return sorted(ret, key=lambda x:(x[2], x[0], x[1]))
    

# Queue 사용하면 안됨
def helper(x, y, shark_size):
    ret = 0
    eaten_fish_count = 0
    
    while 1:
        has_fish = find_short_dist(x, y, shark_size)
        
        if not has_fish:
            break
        
        nx, ny, dist = has_fish.pop(0) # 맨 앞의 물고기 꺼냄
        
        eaten_fish_count += 1 # 물고기 냠
        ret += dist # 물고기를 잡아먹을 수 있는 시간 추가
        
        
        graph[x][y], graph[nx][ny] = 0, 0 # 원래 상어의 위치 빈칸, 먹힌 물고기도 빈칸, 
        x, y = nx, ny # 상어의 위치 갱신
        
        # 자신의 크기와 같은 수의 물고기를 먹었다면
        if eaten_fish_count == shark_size:
            shark_size += 1 # 상어 크기 1 증가
            eaten_fish_count = 0
                
    return ret

n = int(input())

graph = []

# 방향 정보(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    input_data = list(map(int, input().split()))
    graph.append(input_data)

# 상어의 초기 위치 찾기
sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = i, j
            
# BFS?
ret = helper(sx, sy, 2)

# 출력
print(ret)
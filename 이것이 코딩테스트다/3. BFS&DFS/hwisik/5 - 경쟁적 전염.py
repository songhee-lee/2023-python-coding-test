'''
1. 서로 다른 종류의 바이러스들의 위치를 우선순위에 따라 저장한다.
2. 현재 큐의 크기만큼, 바이러스를 하나씩 꺼내면서, 퍼트린다.
'''

from collections import deque

# 현재 위치의 범위 확인
def is_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: return False
    return True

# BFS
def bfs():
    queue = deque() 
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                queue.append((i, j, graph[i][j])) # 바이러스의 위치와 타입을 저장한다.
                
    # 번호가 낮은 순으로 바이러스를 정렬한다.(문제의 조건)
    queue = deque(sorted(list(queue), key=lambda x:x[2]))
    
    
    time = 0 # 흐른 시간
    while queue:
        
        if time == s:
            break
        
        queue_len = len(queue) # 전파 가능한 바이러스의 수(=현재 큐의 크기)
        
        for _ in range(queue_len):
            x, y, virus_type = queue.popleft() # 현재 바이러스 위치, 타입
            
            # (상, 하, 좌, 우) 확인
            for i in range(4): 
                nx, ny = x + dx[i], y + dy[i] # 다음 칸
                if not is_range(nx, ny): continue
                if graph[nx][ny] != 0: continue # 바이러스가 없는 칸이 아니면 전파 불가능
                
                graph[nx][ny] = virus_type # 해당 바이러스 타입으로 전파
                queue.append((nx, ny, virus_type))
        time += 1 # 1초가 흘렀다.
        
# 입력
n, k = map(int, input().split())

# 바이러스 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

# 입력
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

s, x, y = map(int, input().split())

bfs() # bfs 수행

# 출력
print(graph[x - 1][y - 1]) # x초 뒤, (x, y) 칸의 바이러스 타입 
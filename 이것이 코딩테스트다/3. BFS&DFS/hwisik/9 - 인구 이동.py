'''
1. 국경을 공유한 적이 없는 국가들을 순회하면서, 연합이 가능한 국가들을 찾는다.
2. 만약, 연합이 가능한 국가가 있다면, 연합을 이루는 국가의 인구수를 갱신한다.
    2-1. 그렇지 않으면, 반복문을 종료하고  인구 이동 횟수를 출력한다.
3. 연합을 이루는 국가가 없을 때 까지 (1)로 돌아가 반복한다.
'''
from collections import deque

# 현재 위치의 범위 확인
def is_range(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: return False
    return True

# 연합 만들기(or 국경선 열기) - BFS
def make_union(x, y):
    queue = deque()
    border = [] # 국경선을 공유하는 국가 배열
    
    queue.append((x, y))
    border.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if not is_range(nx, ny): continue
            if not l <= abs(graph[nx][ny] - graph[x][y]) <= r: continue
            if visited[nx][ny]: continue
            
            visited[nx][ny] = 1 # 국경선 공유했음
            queue.append((nx, ny))
            border.append((nx, ny))
            
    return border

n, l, r = map(int, input().split())



# 방향 정보 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

move_population_cnt = 0 # 인구 이동 횟수

while 1: # 인구 이동이 더 이상 없을 때까지
    visited = [[0] * n for _ in range(n)]
    can_make_union = False # 연합을 만들 수 있는지
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]: # 국경선을 공유하지 않은 국가일 때
                visited[i][j] = 1
                border = make_union(i, j) # 국경선을 공유하는 국가들
                
                # 국경선이 열렸다면
                if len(border) > 1: 
                    can_make_union = True
                    union_population = sum(graph[x][y] for x, y in border) // len(border) # (연합의 인구 수) / (연합을 이루는 칸의 개수)
                    
                    for x, y in border:
                        graph[x][y] = union_population # 인구 이동
                        
    # 연합을 만들 수 없다면
    if not can_make_union:
        break
    
    move_population_cnt += 1
    
print(move_population_cnt) # 인구 이동 횟수 출력
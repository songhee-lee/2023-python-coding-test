'''
1. 값이 '0'인 특정 노드를 방문한다.
2. 범위를 벗어나지 않고, 값이 '0'인 연결되어 있는 모든 노드를 방문한다.
3. 값이 '0'인 노드를 전부 방문할 때 까지 (1)을 반복한다.
'''
# 현재 위치의 범위 확인
def is_range(x, y): 
    if x < 0 or x >= n or y < 0 or y >= m: return False
    return True

# DFS
def dfs(x, y): 
    frame[x][y] = '-1' # 방문했음을 표시
    for i in range(4): # 상, 하, 좌, 우 확인
        nx, ny = x + dx[i], y + dy[i]
        
        if not is_range(nx, ny): continue # 범위를 벗어난다면
        if frame[nx][ny] != '0': continue # 이미 방문했거나 칸막이라면
        
        dfs(nx, ny) # 재귀 호출
        
n, m = map(int, input().split())

frame = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ret = 0

for _ in range(n):
    data = list(input().rstrip())
    frame.append(data)

for i in range(n):
    for j in range(m):
        if frame[i][j] == '0': # 구멍이 뚫려 있는 부분이라면
            dfs(i, j) # dfs 수행
            ret += 1 # 결과값 1 증가

print(ret)
            
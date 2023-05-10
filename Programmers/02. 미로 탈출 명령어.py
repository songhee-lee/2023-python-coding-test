from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

dx, dy = [1, 0, 0, -1], [0, -1, 1, 0] # 하, 좌, 우, 상
alp = ["d", "l", "r", "u"]
answer = 'z' # 사전 순 비교를 위해 'z'로 초기화

# 범위 확인
def is_range(x, y, n, m):
    return 1 <= x <= n and 1 <= y <= m

# DFS
def dfs(n, m, x, y, r, c, k, way, dist):
    global answer
    
    # 현재까지 이동한 거리에 현재 위치에서 목적지까지의 거리의 합이 k보다 커진다면
    # 즉, 현재지점이 목적지에서 멀어지면
    if k < dist + abs(x - r) + abs(y - c):
        return
    
    # 도착지에 도착하고 이동한 거리가 k일 때
    if x == r and y == c and dist == k:
        answer = way
        return
        
    # [하, 좌, 우, 상]으로 이동
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # 다음 위치가 범위에 속하고 사전순으로 빠를 경우에만 
        if is_range(x, y, n, m) and way < answer:
            dfs(n, m, nx, ny, r, c, k, way + alp[i], dist + 1) # 재귀호출
        
def solution(n, m, x, y, r, c, k):
    total_dist = abs(x - r) + abs(y - c) # 시작점에서 목적지까지의 거리
    
    # 이동해야 하는 거리가 K보다 크면, 이동 불가능
    # K가 더 클 때, K에서 이동해야 하는 거리를 뺐을 때 2의 배수여야 목적지로 돌아올 수 있음
    if total_dist > k or (k - total_dist) % 2 == 1:
        return "impossible"
    
    dfs(n, m, x, y, r, c, k, "", 0)
    
    return answer if answer else "impossible"
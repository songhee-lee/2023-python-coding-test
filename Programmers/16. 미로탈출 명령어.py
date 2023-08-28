"""
- nxm 격자 미로 (x,y) -> (r,c) 
- 총 거리 k (같은 격자 여러번 방문 가능)
- 문자열 사전 순으로 가장 빠른 경로로 탈출
- d l r u
"""
import sys
sys.setrecursionlimit(10**6)

answer = []
move = ['d', 'l', 'r', 'u']
dx = (1, 0, 0, -1)
dy = (0, -1, 1, 0)
def dfs(n, m, x, y, r, c, k, path) :
    global answer
    if abs(x-r)+abs(y-c) > k :          # 도달 불가능한 경우
        return
    if answer :
        return
    
    if (x==r) and (y==c) and k == 0 :   # 도달한 경우
        answer.append(path)
        return
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 1 <= nx <= n and 1 <= ny <= m :
            dfs(n, m, nx, ny, r, c, k-1, path+move[i])

def solution(n, m, x, y, r, c, k):
    # 총 거리 k로 탈출 가능한지 확인
    path = abs(r-x)+abs(c-y)
    if k < path or (k-path) % 2 != 0 :
        return "impossible"
    
    # 탈출 경로 확인
    dfs(n, m, x, y, r, c, k, '')
    return sorted(answer)[0]
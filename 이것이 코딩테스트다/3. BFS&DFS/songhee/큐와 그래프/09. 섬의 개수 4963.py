""" 
- 1초 / 128MB

"""
import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    maps[x][y] = -1
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] == 1:
            dfs(nx, ny)
    
while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0:   # 테스트 종료 조건
        break
    
    maps = []   # 지도 
    for _ in range(H):
        maps.append(list(map(int, sys.stdin.readline().split())))

    # 상하좌우 대각선 이동
    dx = (-1, 1, 0, 0, -1, -1, 1, 1)
    dy = (0, 0, -1, 1, -1, 1, 1, -1)

    count = 0   # 섬의 개수
    for i in range(H):
        for j in range(W):
            if maps[i][j] == 1:
                dfs(i, j)
                count += 1
    
    print(count)
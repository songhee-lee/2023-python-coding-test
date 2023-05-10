""" 

1. 입력 받기
    - 얼음 틀의 세로 N, 가로 M
    - 얼음 틀 0 뚫린 부분 1 칸막이
2. 얼음 틀 방문하기
    - (1, 1) ~ (N, M) 까지 한 칸씩 순서대로 방문
    - 각 칸에서 상/하/좌/우로 이동 가능한 선에서 방문하고 방문 처리하기
"""

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M :
        return False
    
    if ice[x][y] == 0 :
        ice[x][y] = 1   # 해당 칸 방문 처리
        dfs(x-1, y)     # 상, 하, 좌, 우 위치로 이동
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    
    return False

# 1. 입력 받기
N, M = map(int, input().split())    # 세로 길이, 가로 길이

ice = []    # 얼음 틀
for _ in range(N):
    ice.append(list(map(int, input())))

# 2. 얼음 틀 방문하기
# (1, 1) ~ (n, m) 까지 얼음 틀 체크하기
count = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)
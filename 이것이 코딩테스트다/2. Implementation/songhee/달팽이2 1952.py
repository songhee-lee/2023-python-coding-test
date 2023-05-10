"""Psuedo Code

1. M줄 N칸 입력 받기
2. 꺾이는 순간 카운트 하기
    - 4번 꺾여서 원래 방향으로 돌아옴
"""


# 1. 입력 받기
row, col = map(int, input().split())

# 2. 맵 그리기
maps = [ [0 for _ in range(col)] for _ in range(row)]
maps[0][0] = 1

dr = (0, 1, 0, -1) # 우, 하, 좌, 상
dc = (1, 0, -1, 0)

x, y = 0, 0 # 현재 위치
d = 0       # 현재 방향
count = 0   # 방향 전환 횟수
num = 1     # 지나간 칸 개수
    
while True:

    dx, dy = x+dr[d], y+dc[d]

    # 갈 수 있으면 go
    if 0 <= dx < row and 0 <= dy < col and maps[dx][dy] == 0:  
        x, y = dx, dy
        maps[x][y] = 1
        num += 1
    # 못가면 방향 전환
    else:   
        d = (d+1) % 4
        count += 1

    # 맵 전체 다 방문했는 지 확인
    if num == row * col:
        break

print(count)


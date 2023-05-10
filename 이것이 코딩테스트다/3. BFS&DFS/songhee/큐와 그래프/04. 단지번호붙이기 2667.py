""" 
- 1초 / 128MB

- 연결된 그래프끼리 단지 번호 붙인 후, 각 단지에 속하는 집의 수 출력하기
"""

def dfs(x, y):
    # 현재 노드 방문 처리
    graph[x][y] = -1

    # 숫자 세기
    global count
    count += 1

    # 상하좌우 확인
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            dfs(nx, ny)

N = int(input())
graph = []          # 그래프
for _ in range(N):
    graph.append( list(map(int, input())))

# 상하좌우 이동 좌표 
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

result = [] # 결과
count = 0   # 하나의 단지 내 집 개수

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0

print(len(result))  # 총 단지 수
result.sort()       # 단지내 집의 수 오름차순 정렬해 출력
for i in range(len(result)):
    print(result[i])
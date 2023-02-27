'''
주어진 문제는 인접한 국가들끼리 인구 이동을 하며,
이동이 불가능할 때까지 이동을 반복하고,
총 몇 번 이동하는지를 구하는 문제

우선 BFS 알고리즘을 이용하여 인접한 국가들을 탐색하며,
인구 이동이 가능한 경우를 탐색
이 때 인구 이동이 가능한지 여부는 현재 국가와 인접한 국가들의 인구 수 차이가 L 이상 R 이하인지를 검사

인구 이동이 가능한 경우, 해당 국가들은 하나의 연합으로 묶이게 되며,
이 연합의 총 인구 수와 국가들의 좌표를 저장
이후에는 해당 연합에 속한 국가들의 인구 수를 조정
이때, 인구 수 조정을 하기 위해 총 인구 수를 연합에 속한 국가의 수로 나누기
'''
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 지도 정보 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 방향 벡터 (북, 동, 남, 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# (x, y) 위치에서 bfs를 수행하고, 인구 이동이 가능한 모든 칸을 업데이트


def bfs(x, y):
    q = deque()
    q.append((x, y))
    union = []
    union.append((x, y))
    visited[x][y] = True
    total = graph[x][y]  # 인구 수 합계
    count = 1  # 인구 이동이 가능한 칸의 개수
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 방문하지 않았고, 인구 차이가 L 이상 R 이하인 경우에만 큐에 추가
            if not visited[nx][ny] and l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                visited[nx][ny] = True
                q.append((nx, ny))
                union.append((nx, ny))
                total += graph[nx][ny]
                count += 1
    # 인구 이동이 가능한 나라가 하나 이상인 경우, 평균값으로 인구 이동 처리
    if count > 1:
        avg = total // count
        for x, y in union:
            graph[x][y] = avg
        return True
    # 인구 이동이 불가능한 경우
    return False

# 인구 이동이 가능한 나라가 있는지 확인


def check():
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j):
                    return True
    return False


result = 0  # 인구 이동이 일어나는 날짜 수
while True:
    visited = [[False] * n for _ in range(n)]
    if not check():
        break
    result += 1

print(result)

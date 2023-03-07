""" 
- 2초 / 512MB

- 각 역과 순환선 사이의 거리 구하기
    - 순환선의 노드는 각 2개의 간선을 갖는다
    - 순환선의 노드 중 지선의 시작점은 3개 이상의 간선을 갖는다

+ 순환선의 개수가 2개 이상일 경우?
    -> 간선의 개수와 정점의 개수가 같은 연결 그래프는 하나의 사이클을 갖는다.
+ 지선의 시작점이 순환선에 포함되지 않는 경우!! (예제 5)
    -> 순환선에서 포함되는 지선 시작점만 모아야 함
"""

import sys
from collections import deque
sys.setrecursionlimit(10000)

# 순환선 존재하는지 확인하기
def check_cycle(start, now, cnt, stations):
    global in_cycle

    # 2개 이상 방문 후 되돌아온 경우 (싸이클인 경우)
    if start == now and cnt >= 2:
        in_cycle = set(stations)
        return
    
    visited[now] = True
    for i in graph[now]:
        # 탐색 진행
        if not visited[i]:
            check_cycle(start, i, cnt+1, stations+[i])
        elif i == start and cnt >= 2:
            check_cycle(start, i, cnt, stations)



# 1. 입력 받기
N = int(input())    # 역의 개수
graph = [ [] for _ in range(N+1) ]
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 2. 순환선 구하기
in_cycle = set()        # 순환선 표시
distance = [0] * (N+1)  # 거리 표시
branch = set()          # 지선 시작점 위치

for i in range(1, N+1):
    visited = [False] * (N+1)
    check_cycle(i, i, 0, [i])

    if len(in_cycle):
        break

# 3. 지선에 속한 역의 거리 구하기
# 지선 시작점 위치 기록
for i in range(1, N+1):
    if i in in_cycle and len(graph[i]) > 2:
        branch.add(i)

# 거리 구하기
for b in branch:
    q = deque([b])

    while q:
        now = q.pop()

        for i in graph[now]:
            # 순환선에 포함되지 않고, 방문하지 않은 역인 경우
            if i not in in_cycle and distance[i] == 0:
                q.append(i)
                distance[i] = distance[now] + 1

# 4. 각 역과 순환선 사이의 거리 출력
print(*distance[1:])
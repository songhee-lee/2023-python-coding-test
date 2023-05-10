'''

[설명]
- N개의 섬이 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있다.
- 각각의 다리마다 중량제한이 있다.
- 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너진다.
- '한 번의 이동'에서 옮길 수 있는 물품들의 중량의 최댓값을 구하라
    - 서로 같은 두 섬 사이에 여러 개의 다리가 있을 수 있으며, 모든 다리는 양방향이다.

[아이디어]
- '한 번의 이동'에서 옮길 수 있는 물품들의 중량의 최댓값을 구하라
    -> '처음 섬에서 특정 중량으로 출반시킨 짐이 목표 섬까지 도착하는 경로'를 의미한다.
    
- 양방향 & 두 섬 사이의 정보 -> BFS 
- C의 최댓값은 1,000,000,000 -> 이분 탐색 

- 일반적인 이분 탐색 알고리즘으로, 중량의 중간값(mid) 정한 후, BFS를 수행한다.
    - BFS 내에서, 시작점(fx)부터 연결된 노드를 살피면서 다리의 중량제한과 중간값(mid)를 비교한다.
    - 방문하지 않았고, 다리의 중량제한이 중간값(mid)보다 크다면 큐에 넣는다.
    - 큐가 비지 않을 때 까지 위의 과정을 반복한다.
- 단, 끝점에 도달했을 경우 True를 반환한다. -> 특정 중량으로 끝점까지 이동할 수 있다.
- 그게 아니라면 False를 반환한다. -> 특정 중량으로 끝점까지 이동할 수 없다.

'''

import sys
from collections import deque

# 이분 탐색
def binary_search():
    l, r = 1, 1_000_000_000 

    while l <= r:
        mid = l + (r - l) // 2
        # 만약, 특정 중량으로 물품을 옮길 수 있으면, 오른쪽 부분 탐색
        # 물품의 중량을 더 높일 수 있다.
        if bfs(mid):
            l = mid + 1
        # 옮길 수 없다면, 왼쪽 부분 탐색
        # 물품의 중량을 줄여야 한다.
        else: 
            r = mid - 1

    return r

# BFS
def bfs(target):
    q = deque([fx]) # 시작점 삽입
    
    # 방문 처리 리스트 초기화
    visited = [0 for _ in range(n + 1)]
    visited[fx] = 1 
    
    while q:
        cur = q.pop()
        
        # 끝점에 도달했으면(이동 경로가 있다면)
        if cur == fy: return True
        
        # 연결된 다리 확인한다.
        for weight, nxt in graph[cur]:
            if visited[nxt]: continue # 방문한 적이 있다면
            if weight < target: continue # 다리의 중량제한이 특정 중량보다 작다면
            
            visited[nxt] = 1
            q.append(nxt)
    
    # 끝점에 도달할 수 없다.        
    return False


n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    # A번 섬과 B번 섬 사이에 중량제한이 C인 다리
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

# 공장이 위치해 있는 섬의 번호
fx, fy = map(int, sys.stdin.readline().split())

# 이분 탐색 & BFS 수행
ret = binary_search()

# 출력
print(ret)
"""
- 1~n 번호가 적힌 n개의 노드가 있는 그래프가 있다. 
- 2 <= N <= 20,000
- 1 <= edge <= 50,000 
- 1번 노드에서 가장 멀리 떨어진 노드의 갯수 구하기 (최단경로 이동 시 간선 개수가 가장 많은 것)

- 최장 거리 구하기 문제 -> BFS/DFS 로 깊이 확인하고, 최댓값 카운팅하기.
"""
from collections import deque

def solution(n, edge):
    INF = 1e9

    distance = [INF] * (n+1)
    graph = [ [] for _ in range(n+1)]
    for a, b in edge :
        graph[a].append(b)
        graph[b].append(a)    
    
    q = deque([(1, 0)])  # 1번 노드에서 시작
    distance[0] = distance[1] = 0
    while q :
        now, dist = q.popleft()
        
        for nxt in graph[now] :
            if distance[nxt] == INF : # 아직 방문하지 않은 노드인 경우
                distance[nxt] = dist+1
                q.append((nxt, dist+1))
    
    return distance.count(max(distance))
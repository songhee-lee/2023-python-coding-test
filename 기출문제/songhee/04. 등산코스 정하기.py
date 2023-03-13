""" 
- 출입구 gates, 쉼터 (나머지), 산봉우리 summits (양방향 통행 가능)
- 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensity

- 출입구에서 출발해 산봉우리 중 한 곳만 방문한 뒤 원래 출입구로 돌아오기
    -> intensity 최소가 되도록 정하기
- 같은 값 있으면 산봉우리 번호가 낮은 것을 선택
"""

import heapq

def solution(n, paths, gates, summits):
    
    INF = int(1e9)
    gates, summits = set(gates), set(summits)
    graph = [ [] for _ in range(n+1)] # 그래프
    for a, b, c in paths:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    # 최단 경로 구하기
    def dijkstra(start):
        q = []  # (거리, node)
    
        # 시작 노드 
        heapq.heappush(q, (0, start))
        intensity[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)

            # 이미 처리된 노드 또는 산봉우리는 무시하기
            if intensity[now] < dist or now in summits:
                continue

            for node, cost in graph[now]:
                # 출입구면 무시하기
                if node in gates : continue
                    
                cost = max(dist, cost)

                if cost < intensity[node]:
                    intensity[node] = cost
                    heapq.heappush(q, (cost, node))

    result = []
    res = INF
    
    for i in gates:
        # intensity[i] = 출입구에서 i번 까지의 최소 intensity 
        intensity = [res] * (n+1)  
        intensity[0] = INF
        dijkstra(i)
        
        for j in sorted(list(summits)):
            if intensity[j] < res:
                res = intensity[j]
                result.append((j, res))
        
    result = sorted(result, key=lambda x: (x[1], x[0]))
    return result[0]

print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [2], [3, 4]))
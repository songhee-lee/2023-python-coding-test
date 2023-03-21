'''
- 출발지 ~ 산봉우리까지 최소 intensity로만 이동하면 된다. 도착지로 돌아가는 경우는 출발지 ~ intensity의 경로와 동일하게 가면 됨. -> (intensity ~ 도착지는 고려안해도 됨!)
- 다익스트라 알고리즘 사용
-> ✅다시풀기
'''
from collections import deque
from heapq import heappop, heappush

# n : 노드 수
# paths : 등산로 정보
# gates : 출입구
# summits : 산봉우리
def solution(n, paths, gates, summits):
    def get_min_intensity():
        pq = [] # (intensity, 현재 위치)
        dist = [1e7 + 1] * (n + 1) # 특정 노드까지 가는데 필요한 최소 intensity(다익스트라)
        
        # 모든 출발지를 우선순위 큐에 삽입
        for gate in gates:
            dist[gate] = 0
            heappush(pq, (dist[gate], gate))
        
        # 산봉우리에 도착할 때 까지 반복
        while pq:
            intensity, node = heappop(pq)
            
            # 산봉우리 or 현재 intensity보다 더 큰 intensity라면 이동 X
            if node in summits_set or dist[node] < intensity:
                continue
            
            # 현재 위치에서 이동할 수 있는 곳 찾아서 이동
            for w, nxt in graph[node]:
                
                # 다음 위치에 더 작은 intensity로 도착할 수 있으면 큐에 넣지 X
                # 출입구는 0으로 설정했기 떄문에, 방문 X
                new_intensity = max(intensity, w)
                if new_intensity < dist[nxt]:
                    dist[nxt] = new_intensity
                    heappush(pq, (new_intensity, nxt))

        # intensity 중 가장 작은 값 반환
        ret = [summits[0], dist[summits[0]]]
        for summit in summits:
            if dist[summit] < ret[1]:
                ret[0] = summit
                ret[1] = dist[summit]

        return ret
    
    summits.sort()
    summits_set = set(summits)
    
    # 등산로 정보
    graph = [[] for _ in range(n + 1)]
    
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    
    # 최소 intensity 반환
    return get_min_intensity()
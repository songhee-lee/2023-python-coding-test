import heapq

INF = int(1e9)
def solution(n, paths, gates, summits):
    # 다익스트라
    def dijkstra():
        q = []
        dist = [INF] * (n + 1) # 거리 정보 초기화
        
        # 모든 출입구 넣기
        for gate in gates:
            dist[gate] = 0
            heapq.heappush(q, (0, gate))
        
        while q:
            intensity, cur = heapq.heappop(q)
            
            # 최소 intensity를 구해야 하므로
            # 산봉우리거나 더 큰 intensity라면 이동하지 않는다.
            if cur in summits_set or dist[cur] < intensity:
                continue
            
            # 이동해본다.
            for w, nxt in edges[cur]:
                new_intensity = max(w, intensity) # 휴식없는 가장 긴 시간이므로
                
                # new_intensity는 확인할 경로의 intensity이고
                # dist[nxt]는 이미 저장된 nxt까지의 경로의 intensity이다.
                # nxt 위치에 더 작은 intensity로 도착한 적이 있다면
                # 큐에 넣지 않는다.
                if new_intensity < dist[nxt]:
                    dist[nxt] = new_intensity
                    heapq.heappush(q, (new_intensity, nxt))
        
        # 최소 intensity 찾기
        ret = [summits[0], dist[summits[0]]]
        for summit in summits:
            if dist[summit] < ret[1]:
                ret[0] = summit
                ret[1] = dist[summit]
                
        return ret
    
    # intensity가 최소가 되는 산봉우리가 여러 개일 때
    # 산봉우리의 번호가 가장 낮은 등산코스를 선택하기 위해 정렬
    summits.sort()
    summits_set = set(summits)
    edges = [[] for _ in range(n + 1)]
    
    # 양방향 등산로 정보 초기화
    for path in paths:
        i, j, w = path
        edges[i].append((w, j))
        edges[j].append((w, i))
    
    answer = dijkstra()
    
    return answer
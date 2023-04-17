import heapq, sys

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수, 메시지를 보내고자 하는 도시 C를 입력받기
n, m, c = map(int, sys.stdin.readline().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] * (n + 1) for _ in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        d, cur = heapq.heappop(q) 
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dist[cur] < d:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for nxt in graph[cur]:
            cost = d + nxt[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[nxt[0]]:
                dist[nxt[0]] = cost
                heapq.heappush(q, (cost, nxt[0]))

# 다익스트라 알고리즘을 수행
dijkstra(c)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_dist = 0

for i in range(1, n + 1):
    # 도달할 수 있는 노드인 경우
    if dist[i] != INF:
        count += 1
        max_dist = max(max_dist, dist[i])

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_dist)
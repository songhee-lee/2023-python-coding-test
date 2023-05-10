import heapq, sys

# 1. 다익스트라 알고리즘
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, sys.stdin.readline().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
_graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF] * (n + 1)
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [0] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 양방향이고, 모든 거리는 1이므로
    _graph[a].append((b, 1))
    _graph[b].append((a, 1))

# 거쳐가야 하는 노드와 목적지 노드를 입력받기
x, k = map(int, sys.stdin.readline().split())

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    
    for i in range(1, n + 1):
        if dist[i] < min_value and not visited[i]:
            min_value = dist[i]
            index = i
            
    return index

def dijkstra(start, end):
    # 시작 노드에 대해서 초기화
    dist[start] = 0
    visited[start] = 1
    
    for node in _graph[start]:
        dist[node[0]] = 1
    
    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for _ in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        nxt = get_smallest_node()
        visited[nxt] = 1
        
        # 현재 노드와 연결된 다른 노드를 확인
        for node in _graph[nxt]:
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[node[0]] > dist[nxt] + 1:
                dist[node[0]] = dist[nxt] + 1
                
    return dist[end]

# 1 -> k 최단 거리
s_to_k = dijkstra(1, k)

# k -> x 최단 거리를 찾기 위해서 초기화
dist = [INF] * (n + 1)
visited = [0] * (n + 1)

# k -> x 최단 거리
k_to_x = dijkstra(k, x)

# 이동할 수 없다면
if s_to_k + k_to_x >= INF:
    print(-1)
# 이동할 수 있다면
else:
    print(s_to_k + k_to_x)

# 2. 개선된 다익스트라 알고리즘

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, sys.stdin.readline().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
_graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    _graph[a].append((b, 1))
    _graph[b].append((a, 1))

x, k = map(int, sys.stdin.readline().split())


def dijkstra(start, end):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    dist[start] = 0
    
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        d, now = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dist[now] < d:
            continue
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in _graph[now]:
            cost = d + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return dist[end]

s_to_k = dijkstra(1, k)

dist = [INF] * (n + 1)

k_to_x = dijkstra(k, x)

if s_to_k + k_to_x >= INF:
    print(-1)
else:
    print(s_to_k + k_to_x) 
            
# 3. 플로이드 워셜 알고리즘

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, sys.stdin.readline().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
_graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            _graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b = map(int, sys.stdin.readline().split())
    _graph[a][b] = 1
    _graph[b][a] = 1
    
x, k = map(int, sys.stdin.readline().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            _graph[a][b] = min(_graph[a][b], _graph[a][k] + _graph[k][b])

# 수행된 결과를 출력
dist = _graph[1][k] + _graph[k][x]

if dist >= INF:
    print(-1)
else:
    print(dist)

import heapq

INF = int(1e9)  # 무한대 값 설정

n, m, k, x = map(int, input().split())  # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호 입력
graph = [[] for _ in range(n+1)]  # 각 도시와 연결된 도시와 그 거리 정보를 담을 리스트

# 모든 도로 정보입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))  # 거리는 1로 고정

# 최단 거리 정보를 담을 리스트 초기화
distance = [INF] * (n+1)
distance[x] = 0  # 출발 도시의 거리는 0으로 설정

# 다익스트라 알고리즘 구현
q = []
heapq.heappush(q, (0, x))  # 우선순위 큐에 출발 도시를 추가

while q:
    dist, now = heapq.heappop(q)
    # 이미 처리된 노드면 무시
    if distance[now] < dist:
        continue
    # 현재 노드와 연결된 다른 노드들의 거리를 계산
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

# 최단 거리가 k인 도시의 번호 출력
result = []
for i in range(1, n+1):
    if distance[i] == k:
        result.append(i)

# 최단 거리가 k인 도시가 없는 경우 -1 출력
if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)

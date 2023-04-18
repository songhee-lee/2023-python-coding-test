### Shortest Path

- 가장 짧은 경로를 찾는 알고리즘
- 상황에 맞는 효율적인 알고리즘이 이미 정립되어 있다.
- 학부 수준에서는 `다익스트라`, `플로이드 워셜`, `벨만 포드` 3가지 사용



### 다익스트라 Dijkstra

- 특정 노드에서 출발해 다른 노드로 가는 각각의 최단 경로 구하는 알고리즘
- 음의 간선이 없을 때 동작
- 현실 세계는 음의 간선으로 표현되지 않아 실제 GPS 소프트웨어의 기본 알고리즘으로 채택되곤 함
- 그리디 알고리즘으로 분류되며, 매번 가장 비용이 적은 노드를 선택하는 과정을 반복함

<br>

```text
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
4. 해당 노트 거쳐 다른 노드로 가는 비용을 계산해 최단 거리 테이블 갱신
5. 3~4 반복
```

- 단계마다 모든 노드를 확인하는 O(V^2) 으로 구현할 수 있음
- 힙 자료구조 이용해 O(ElogV) 로 구현 가능

<br>

```python
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())	# 노드 개수, 간선 개수
start = int(input())							# 시작 노드 번호
grpah = [[] for i in range(n+1)]	# 그래프 
distance = [INF] * (n+1)					# 최단 거리 테이블

# 그래프 입력 받기
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))	# a-> b 가는 비용이 c
 
def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정한 후 큐에 삽입
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
    dist, now = heapq.heapop(q)
    # 현재 노드가 이미 처리된 적 있는 노드라면 무시
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 다른 인접한 노드들 확인
    for i in graph[now]:
      cost = dist + i[1]
      # 현재 노드 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
      
dijstra(start)
```

<br><br>



### 플로드 워셜 Floyd-Warshall

- 모든 지점에서 다른 모든 지점까지의 최단 경로를 구하는 알고리즘
- 시간 복잡도 : O(N^3)
- Dab = min(Dab, Dak + Dkb)

<br>

```python
INF = int(1e9)

n, m = map(int, input().split())	# 노드 개수, 간선 개수
# 그래프 초기화
graph = [[INF]* (n+1) for _ in range(n+1)]	
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b :
      graph[a][b] = 0

# 그래프 입력 받기
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c 		# a-> b 비용은 c
  
# 점화식 따라 플로드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
```


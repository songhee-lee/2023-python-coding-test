### 기타 그래프 이론



### 서로소 집합 Disjoint set = 유니온 파인드 Union-find

- 수학에서 서로소 집합은 공통 원소가 없는 두 집합을 의미한다.
- `서로소 집합 자료구조`는 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조로 `union`과 `find` 2개의 연산으로 조작한다.

- 시간복잡도 : O(V + M(1+log_(2-M/V) V))
  - 노드 개수가 V개이고, 최대 V-1개의 union 연산과 M개의 find 연산이 가능할 때, 경로 압축 방법을 적용한 시간복잡도
  - V = 1000, find/union 연산 100만 번일 때, 약 1,000만 번의 연산 필요

<br>

```python
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x) :
	# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
   return parent[x]

# 두 원소가 속한 집합 찾기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드 개수와 간선 개수 입력 받기
v, e = map(int, input().split())

# 부모 테이블을 자기 자신으로 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
  parent[i] = i

# union 연산 수행
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)
```

<br>

<br>

### 신장 트리 Spanning Tree

- 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

<br>

#### 크루스칼 Kruskal

- 대표적인 최소 신장 트리 알고리즘
  - 가장 적은 비용으로 모든 노드를 연결하는 알고리즘

- 그리디 알고리즘
  - 모든 간선에 대해 정렬을 수행한 뒤, 가장 거리가 짧은 간선부터 집합에 포함시킨다.
  - 이때, 사이클을 발생시킬 수 있는 간선의 경우 집합에 포함시키지 않는다.
- 시간 복잡도 : O(ElogE)
  - 간선 개수 E

<br>

```python
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  # 루트 노드가 아니라면 루트 노드 찾을 때까지 재귀적으로 호출
  if parent[x] != x :
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
# 노드 개수와 간선 개수 입력 받기
v, e = map(int, input().split())

# 부모 테이블을 자기 자신으로 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
  parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 간선 정보 입력받기
for _ in range(e):
  a, b, c = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()		# 간선 비용순으로 정렬

# 간선 하나씩 확인하면서
for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
```

<br><br>

### 위상정렬 Topology Algorithm

- 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
- 시간 복잡도 : O( V+E )

- 알고리즘

  1. 진입차수가 0인 노드를 큐에 넣는다.

  2. 큐가 빌 때까지 다음을 반복한다

     - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다

     - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

<br>

```python
from collections import deque

# 노드 개수와 간선 개수 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v+1)]

# 간선 정보 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)	# a->b
  indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
  result = []
  q = deque()
  
  # 진입 차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
  
  # 큐가 빌 때까지 반복
  while q:
    now = q.popleft()
    result.append(now)
    # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
    for i in graph[now]:
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)
```


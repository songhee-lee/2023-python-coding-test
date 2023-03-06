
1. [특정 거리의 도시 찾기](#3.-특정-거리의-도시-찾기)
2. [괄호 변환](#6.-괄호-변환)
3. [연산자 끼워넣기](#7.-연산자-끼워넣기)
4. [블록 이동](#10.-블록-이동)
[](#)
[](#)
---


### 3. 특정 거리의 도시 찾기
- `sys.stdin.readline().rstrip().split()` 사용 안하면 시간초과 뜸
- 하나씩 방문하면서 depth 조사하고, K depth 가진 노드 모두 출력함.

<br>

### 6. 괄호 변환
- 재귀 함수 형식을 더 깔끔하게 할 수 있다.

```python
def solution(p):
  if p=='': return p
  r=True; c=0
  for i in range(len(p)):
      if p[i]=='(': c-=1
      else: c+=1
      if c>0: r=False
      if c==0:
          if r:
              return p[:i+1]+solution(p[i+1:])
          else:
              return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
```
<br>

### 7. 연산자 끼워넣기
- `permutations` 로 연산자 순열 구해서 진행하면 `시간 초과`
- 순열은 시간 복잡도가 `O(n!)` 이기 때문에 1초 제한일 때 최대 10까지 가능함

- 파이썬에서 초당 2천만번 연산 가능하다고 가정하는 것이 좋음
```
O(NlogN) : 100,000
O(N^2)   : 2,000
O(N^3)   : 500
O(N!)    : 10
```
<br>

### 10. 블록 이동
- 최단경로와 비슷하므로 bfs로 현재 위치에서 이동 가능한 로봇의 위치 넣기
- 이미 로봇이 위치해서 확인한 경우를 (위치1, 위치2) 형태로 저장하기 
  -> set 타입을 사용해야 시간초과 나지 않음
  - list 에서 `in 연산자`의 시간 복잡도는 `O(N)`
  - set 또는 dict 에서 `in 연산자`의 시간 복잡도는 `O(1)`
=======
- 탐색 : 많은 데이터 중 원하는 데이터를 찾는 과정

- `스택` : LIFO

  - 파이썬의 리스트 사용하면 됨 - append() / pop()

- `큐` : FIFO

  - deque 라이브러리 이용해서 구현 - append() / popleft()

  ```python
  from collections import deque
  
  queue = deque()
  ```

<br><br>



### DFS (Depth Frist Search)

- 재귀적 특징과 백트래킹 이용한 모든 경우를 하나하나 전부 탐색하는 경우 선호(대표적으로 조합 순열 구현)

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택 최상단 노드에 방문하지 않은 인접 노드가 있으면 인접 노드를 스택에 넣고 방문 처리, 없다면 스택에서 최상단 노드 꺼내기
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

```python
def dfs(graph, v, visited):
		# 현재 노드 방문 처리
		visited[v] = True
		print(v, end=' ')
		
		# 인접 노드들 재귀적으로 방문
		for i in graph[v]:
				if not visited[i]:
						dfs(graph, i, visited)
```

<br><br>



### BFS (Breadth First Search)

- 큐 사용해 Depth 특징 이용한 문제 경우 선호 (대표적으로 최단경로)

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드 꺼내서 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복

```python
from collections import deque

def bfs(graph, start, visited):
		queue = deque([start])

		# 현재 노드 방문 처리
		visited[start] = True
		
		while queue:
				v = queue.popleft()
				print(v, end=' ')
				
				for i in graph[v]:
						if not visited[i]:
								queue.append(i)
								visited[i] = True
```

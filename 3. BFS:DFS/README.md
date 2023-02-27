## DFS/BFS
- 탐색 : 많은 데이터 중 원하는 데이터를 찾는 과정
<br>

### DFS (Depth Frist Search)
- 재귀적 특징과 백트래킹 이용한 모든 경우를 하나하나 **전부 탐색하는 경우 선호(대표적으로 조합 순열 구현)**
<br>

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

### BFS (Breadth First Search)
- 큐 사용해 Depth 특징 이용한 문제 경우 선호 **(대표적으로 최단경로)**
<br>

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

<br><br><br>

### 문제

| Name            | 송희       | 숙경       | 주현      | 휘식      |
| --------------- | --------- |---------- | -------- | -------- |
| 음료수 얼려 먹기    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/1%20-%20%EC%9D%8C%EB%A3%8C%EC%88%98%20%EC%96%BC%EB%A0%A4%20%EB%A8%B9%EA%B8%B0.py)    | [code]    | [code]   | [code]   |
| 미로 탈출    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/2%20-%20%EB%AF%B8%EB%A1%9C%20%ED%83%88%EC%B6%9C.py)    | [code]    | [code]   | [code]   |
| 특정 거리의 도시 찾기    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/3%20-%20%ED%8A%B9%EC%A0%95%20%EA%B1%B0%EB%A6%AC%EC%9D%98%20%EB%8F%84%EC%8B%9C%20%EC%B0%BE%EA%B8%B0.py)    | [code]    | [code]   | [code]   |
| 연구소    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/4%20-%20%EC%97%B0%EA%B5%AC%EC%86%8C.py)    | [code]    | [code]   | [code]   |
| 경쟁적 전염    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/5%20-%20%EA%B2%BD%EC%9F%81%EC%A0%81%20%EC%A0%84%EC%97%BC.py)    | [code]    | [code]   | [code]   |
| 괄호 변환    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/6%20-%20%EA%B4%84%ED%98%B8%20%EB%B3%80%ED%99%98.py)    | [code]    | [code]   | [code]   |
| 연산자 끼워 넣기    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/7%20-%20%EC%97%B0%EC%82%B0%EC%9E%90%20%EB%81%BC%EC%9B%8C%20%EB%84%A3%EA%B8%B0.py)    | [code]    | [code]   | [code]   |
| 감시 피하기    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/8%20-%20%EA%B0%90%EC%8B%9C%20%ED%94%BC%ED%95%98%EA%B8%B0.py)    | [code]    | [code]   | [code]   |
| 인구 이동    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/9%20-%20%EC%9D%B8%EA%B5%AC%20%EC%9D%B4%EB%8F%99.py)    | [code]    | [code]   | [code]   |
| 블록 이동    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/10%20-%20%EB%B8%94%EB%A1%9D%20%EC%9D%B4%EB%8F%99.py)    | [code]    | [code]   | [code]   |
| DFS와 BFS    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/DFS%EC%99%80%20BFS%201260.py)    | [code]    | [code]   | [code]   |


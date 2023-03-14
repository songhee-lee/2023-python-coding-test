DFS/BFS

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

| Name                  | 송희                                                         | 숙경                                                         | 주현   | 휘식   |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ | ------ |
| 음료수 얼려 먹기      | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/1%20-%20%EC%9D%8C%EB%A3%8C%EC%88%98%20%EC%96%BC%EB%A0%A4%20%EB%A8%B9%EA%B8%B0.py) | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS%3ADFS/sukkyeong/1.%EC%9D%8C%EB%A3%8C%EC%88%98%EC%96%BC%EB%A0%A4%EB%A8%B9%EA%B8%B0.py) | [code] | [code] |
| 미로 탈출             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/2%20-%20%EB%AF%B8%EB%A1%9C%20%ED%83%88%EC%B6%9C.py) | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS%3ADFS/sukkyeong/2.%EB%AF%B8%EB%A1%9C%ED%83%88%EC%B6%9C.py) | [code] | [code] |
| 특정 거리의 도시 찾기 | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/3%20-%20%ED%8A%B9%EC%A0%95%20%EA%B1%B0%EB%A6%AC%EC%9D%98%20%EB%8F%84%EC%8B%9C%20%EC%B0%BE%EA%B8%B0.py) | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS%3ADFS/sukkyeong/3.%ED%8A%B9%EC%A0%95%EA%B1%B0%EB%A6%AC%EC%9D%98%EB%8F%84%EC%8B%9C%EC%B0%BE%EA%B8%B0.py) | [code] | [code] |
| 연구소                | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/4%20-%20%EC%97%B0%EA%B5%AC%EC%86%8C.py) | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS%3ADFS/sukkyeong/4.%EC%97%B0%EA%B5%AC%EC%86%8C.py) | [code] | [code] |
| 경쟁적 전염           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/5%20-%20%EA%B2%BD%EC%9F%81%EC%A0%81%20%EC%A0%84%EC%97%BC.py) | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS%3ADFS/sukkyeong/5.%EA%B2%BD%EC%9F%81%EC%A0%81%EC%A0%84%EC%97%BC.py) | [code] | [code] |
| 괄호 변환             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/6%20-%20%EA%B4%84%ED%98%B8%20%EB%B3%80%ED%99%98.py) | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS%3ADFS/sukkyeong/6.%EA%B4%84%ED%98%B8%EB%B3%80%ED%99%98.py) | [code] | [code] |
| 연산자 끼워 넣기      | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/7%20-%20%EC%97%B0%EC%82%B0%EC%9E%90%20%EB%81%BC%EC%9B%8C%20%EB%84%A3%EA%B8%B0.py) | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS%3ADFS/sukkyeong/7.%EC%97%B0%EC%82%B0%EC%9E%90%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0.py) | [code] | [code] |
| 감시 피하기           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/8%20-%20%EA%B0%90%EC%8B%9C%20%ED%94%BC%ED%95%98%EA%B8%B0.py) | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS%3ADFS/sukkyeong/8.%EA%B0%90%EC%8B%9C%ED%94%BC%ED%95%98%EA%B8%B0.py) | [code] | [code] |
| 인구 이동             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/9%20-%20%EC%9D%B8%EA%B5%AC%20%EC%9D%B4%EB%8F%99.py) | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS%3ADFS/sukkyeong/9.%EC%9D%B8%EA%B5%AC%EC%9D%B4%EB%8F%99.py) | [code] | [code] |
| 블록 이동             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/10%20-%20%EB%B8%94%EB%A1%9D%20%EC%9D%B4%EB%8F%99.py) | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS%3ADFS/sukkyeong/10.%EB%B8%94%EB%A1%9D%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0.py) | [code] | [code] |
| DFS와 BFS             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/DFS%EC%99%80%20BFS%201260.py) | [code](https://www.acmicpc.net/submit/1260/55152503)         | [code] | [code] |
| 큐                    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/01.%20%ED%81%90%2010845.py) | [code]                                                       | [code] | [code] |
| 덱                    | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/02.%20%EB%8D%B1%2010866.py) | [code]                                                       | [code] | [code] |
| 연결 요소의 개수      | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/03.%20%EC%97%B0%EA%B2%B0%20%EC%9A%94%EC%86%8C%EC%9D%98%20%EA%B0%9C%EC%88%98%2011724.py) ✅ | [code]                                                       | [code] | [code] |
| 단지번호붙이기        | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/04.%20%EB%8B%A8%EC%A7%80%EB%B2%88%ED%98%B8%EB%B6%99%EC%9D%B4%EA%B8%B0%202667.py) | [code]                                                       | [code] | [code] |
| 미로탐색              | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/05.%20%EB%AF%B8%EB%A1%9C%20%ED%83%90%EC%83%89%202178.py) | [code]                                                       | [code] | [code] |
| 나이트의 이동         | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/06.%20%EB%82%98%EC%9D%B4%ED%8A%B8%EC%9D%98%20%EC%9D%B4%EB%8F%99%207562.py) | [code]                                                       | [code] | [code] |
| 순열 사이클           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/07.%20%EC%88%9C%EC%97%B4%20%EC%82%AC%EC%9D%B4%ED%81%B4%2010451.py) | [code]                                                       | [code] | [code] |
| 반복수열              | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/08.%20%EB%B0%98%EB%B3%B5%EC%88%98%EC%97%B4%202331.py) | [code]                                                       | [code] | [code] |
| 섬의 개수             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/09.%20%EC%84%AC%EC%9D%98%20%EA%B0%9C%EC%88%98%204963.py) | [code]                                                       | [code] | [code] |
| Two Dots              | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/10.%20Two%20Dots%2016929.py) | [code]                                                       | [code] | [code] |
| 서울 지하철 2호선     | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/11.%20%EC%84%9C%EC%9A%B8%20%EC%A7%80%ED%95%98%EC%B2%A0%202%ED%98%B8%EC%84%A0%2016947.py) | [code]                                                       | [code] | [code] |
| 줄 세우기             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/12.%20%EC%A4%84%20%EC%84%B8%EC%9A%B0%EA%B8%B0%202252.py) ✅ | [code]                                                       | [code] | [code] |
| 작업                  | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/%ED%81%90%EC%99%80%20%EA%B7%B8%EB%9E%98%ED%94%84/13.%20%EC%9E%91%EC%97%85%202056.py) | [code]                                                       | [code] | [code] |
| 알고스팟              | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/01.%20%EC%95%8C%EA%B3%A0%EC%8A%A4%ED%8C%9F%201261.py) | [code]                                                       | [code] | [code] |
| 데스나이트            | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/02.%20%EB%8D%B0%EC%8A%A4%20%EB%82%98%EC%9D%B4%ED%8A%B8%2016948.py) | [code]                                                       | [code] | [code] |
| 아기 상어             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/03.%20%EC%95%84%EA%B8%B0%20%EC%83%81%EC%96%B4%2016236.py) | [code]                                                       | [code] | [code] |
| 소수 경로             | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/04.%20%EC%86%8C%EC%88%98%20%EA%B2%BD%EB%A1%9C%201963.py) ✅ | [code]                                                       | [code] | [code] |
| 적록색약              | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/05.%20%EC%A0%81%EB%A1%9D%EC%83%89%EC%95%BD%2010026.py) | [code]                                                       | [code] | [code] |
| 연구소                | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/06.%20%EC%97%B0%EA%B5%AC%EC%86%8C%2014502.py) | [code]                                                       | [code] | [code] |
| 아기 상어2            | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/07.%20%EC%95%84%EA%B8%B0%20%EC%83%81%EC%96%B42%2017086.py) | [code]                                                       | [code] | [code] |
| 성곽                  | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/08.%20%EC%84%B1%EA%B3%BD%202234.py) | [code]                                                       | [code] | [code] |
| 새로운 하노이 탑      | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/09.%20%EC%83%88%EB%A1%9C%EC%9A%B4%20%ED%95%98%EB%85%B8%EC%9D%B4%20%ED%83%91%2012906.py) ✅ | [code]                                                       | [code] | [code] |
| 연구소 2              | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/10.%20%EC%97%B0%EA%B5%AC%EC%86%8C2%2017141.py) | [code]                                                       | [code] | [code] |
| 0과 1                 | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/11.%200%EA%B3%BC1%208111.py) ❗ | [code]                                                       | [code] | [code] |
| 체스판 여행 1         | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/12.%20%EC%B2%B4%EC%8A%A4%ED%8C%90%20%EC%97%AC%ED%96%891%2016959.py) | [code]                                                       | [code] | [code] |
| 체스판 여행 2         | [code ](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/13.%20%EC%B2%B4%EC%8A%A4%ED%8C%90%20%EC%97%AC%ED%96%892%2016952.py)✅ | [code]                                                       | [code] | [code] |
| 구슬 탈출 4           | [code](https://github.com/songhee-lee/2023-python-coding-test/blob/main/3.%20BFS:DFS/songhee/BFS/14.%20%EA%B5%AC%EC%8A%AC%20%ED%83%88%EC%B6%9C4%2015653.py) | [code]                                                       | [code] | [code] |




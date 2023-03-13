'''
- 학생을 노드로 보면, 각 노드 사이에는 우선순위가 존재한다.
- 우선순위가 존재하는 노드 사이에는 '위상정렬'을 사용한다.
- 학생들 사이의 키의 관계는 '진입차수'로 볼 수 있다.
    - ex. A가 B앞에 서야 한다 => B의 진입차수는 '1'이다.
            and C가 B 앞에 서야 한다 => B의 진입차수는 1 + 1 = '2'이다.
- 특정 학생의 진입차수가 0이라면, 그 학생은 줄을 세울 때 제약이 없으므로, 우선해서 세울 수 있다.
'''
import sys
from collections import deque

# 위상 정렬
def topology_sort():
    queue = deque()
    
    # 진입 차수가 0인 경우(= 자기 자신 앞에 서는 학생이 없는 경우)
    for i in range(n):
        if indegree[i] == 0: queue.append(i)
    
    # 모든 학생(노드)을 탐색
    for i in range(n):
        if not queue:
            return

        cur = queue.popleft()
        ret.append(cur)
        
        # 연결된 노드 탐색
        for nxt in graph[cur]:
            indegree[nxt] -= 1 # 진입 차수 - 1
            if indegree[nxt] == 0: # 자기 자신 앞에 서는 학생이 없는 경우
                queue.append(nxt)

n, m = map(int, sys.stdin.readline().split())

indegree = [0] * n # 진입 차수
graph = [[] for _ in range(n)] # 노드간의 관계
ret = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1].append(b - 1)
    indegree[b - 1] += 1
    
# 위상 정렬 수행
topology_sort()

# 출력
for x in ret:
    print(x + 1, end=' ')
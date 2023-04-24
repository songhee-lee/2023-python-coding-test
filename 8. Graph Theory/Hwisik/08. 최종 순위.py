'''
- 예를 들어, 작년 팀 순위가 [5 4 3 2 1] 이라면, 5는 4에 대해서만 우선인게 아니라, 4, 3, 2, 1에 대해서도 우선순위가 높다는 뜻이다.
    - 5 : 4, 3, 2, 1
    - 4 : 3, 2, 1
    - 3 : 2, 1
    - 2 : 1
    - 1 : 없음
- 확실한 순위를 찾을 수 없는 경우 -> 발생하지 X -> 작년 순위가 주어졌기 때문?
- 일관성이 없는 경우 -> 사이클이 발생한 경우
'''
import sys
from collections import deque

input = sys.stdin.readline

# 위상 정렬
def topology_sort():
    q = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    # 사이클이 발생한 경우(진입차수가 0인 노드가 없음)
    if not q:
        print("IMPOSSIBLE")
        return

    ret = []
    while q:
        cur = q.popleft()
        ret.append(cur)
        
        for nxt in graph[cur]:
            indegree[nxt] -= 1 # 진입차수 1 감소
            
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[nxt] == 0:
                q.append(nxt)
    
    # 진입차수가 0이 아닌 팀이 존재한다면 -> 사이클이 발생한 경우
    if indegree.count(0) != n + 1:
        print("IMPOSSIBLE")
    else:
        print(*ret) # 리스트를 공백으로 구분하여 출력

tc = int(input())

for _ in range(tc):
    n = int(input())
    teams = list(map(int, input().split())) # 작년 순위
    
    indegree = [0 for _ in range(n + 1)] # 진입차수
    graph = [[] for _ in range(n + 1)] # 간선 정보
    
    # 작년 순위를 기반으로 그래프 생성
    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[teams[i]].append(teams[j])
            indegree[teams[j]] += 1
    
    # 등수가 바뀐 쌍의 개수
    m = int(input())
    
    for _ in range(m):
        # 등수가 바뀐 두 팀
        a, b = map(int, input().split())
        
        # b가 a보다 앞서 있었는데, a가 b보다 앞서게 바뀐 경우
        if a in graph[b]:
            graph[b].remove(a) # b -> a 간선 제거
            graph[a].append(b) # a -> b 간선 추가
            indegree[b] += 1 # b의 진입차수 1 증가
            indegree[a] -= 1 # a의 진입차수 1 감소(a가 b보다 앞서므로)
        else: # 그렇지 않은 경우
            graph[a].remove(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] -= 1
    
    # 위상 정렬 수행
    topology_sort()
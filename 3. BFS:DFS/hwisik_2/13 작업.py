'''
- '줄 세우기' 문제와 유사.
- 수행해야 하는 작업에는 선행 관계가 존재한다. -> 위상 정렬
- K번 작업이 시작되려면, K번 작업의 선행관계에 있는 모든 노드들의 작업이 끝나는 시간들 중, '가장 늦게 끝나는 시간'이 'K번 작업의 시작시간'이 된다. (문제의 설명)
- 모든 작업에 대해, 위상정렬로 필요한 시간들을 구한다.
- 최종적으로, 모든 작업들의 필요한 시간 중 가장 큰 값이 
                모든 작업을 완료하기 위한 최소 시간이 된다.
'''

import sys
from collections import deque

# 위상 정렬
def topology_sort():
    queue = deque()
    
    for i in range(n):
        if indegree[i] == 0: # 선행 관계가 없다면
            queue.append(i)
            ret[i] = need_time[i] # 작업 완료에 필요한 시간 초기화
            
    for _ in range(n):
        cur = queue.popleft()
        
        for nxt in graph[cur]:
            indegree[nxt] -= 1 # 진입차수 - 1
            
            # 작업 완료에 필요한 시간을 갱신(최대 시간으로)
            ret[nxt] = max(ret[nxt], ret[cur] + need_time[nxt]) 
            
            # 선행 관계가 없다면
            if indegree[nxt] == 0:
                queue.append(nxt)
        
n = int(input())

graph = [[] for _ in range(n)] # 노드 관계
indegree = [0] * n # 진입 차수
need_time = [0] * n # 작업에 걸리는 시간
ret = [0] * n # 작업을 완료하기 위한 최소 시간

for i in range(n):
    work_data = list(map(int, sys.stdin.readline().split()))
    
    time = work_data[0] # i번 작업에 걸리는 시간
    preceding_work_count = work_data[1] # i번 작업과 선행 관계에 있는 작업들의 개수
    
    need_time[i] = time
    # 노드 연결하기
    for work in work_data[2:]:
        graph[work - 1].append(i)
        indegree[i] += 1 # 진입차수 + 1

# 위상정렬 수행
topology_sort()

# 모든 작업을 완료하기 위한 최소 시간
print(max(ret))
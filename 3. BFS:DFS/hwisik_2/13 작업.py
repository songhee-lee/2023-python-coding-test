'''
1. 수행해야 하는 작업에는 선행 관계가 존재한다. -> 위상 정렬
2. K번 작업이 시작되려면, K번 작업의 선행관계에 있는 모든 노드들의 작업이 끝나는 시간들 중, '가장 늦게 끝나는 시간'이 'K번 작업의 시작시간'이 된다.
'''

import sys
from collections import deque

def topology_sort():
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
            ret[i] = need_time[i]
    
    for _ in range(n):
        cur = queue.popleft()
        
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            
            ret[nxt] = max(ret[nxt], ret[cur] + need_time[nxt])    
            
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
        indegree[i] += 1

topology_sort()

print(max(ret))
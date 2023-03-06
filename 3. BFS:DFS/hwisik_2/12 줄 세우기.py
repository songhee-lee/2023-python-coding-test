'''

'''
import sys
from collections import deque
def topology_sort():
    queue = deque()
    
    for i in range(n):
        if indegree[i] == 0: queue.append(i)
    
    for i in range(n):
        if not queue:
            return

        cur = queue.popleft()
        ret.append(cur)
        
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

n, m = map(int, sys.stdin.readline().split())

indegree = [0] * n
graph = [[] for _ in range(n)]
ret = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1].append(b - 1)
    indegree[b - 1] += 1
    
topology_sort()

for x in ret:
    print(x + 1, end=' ')
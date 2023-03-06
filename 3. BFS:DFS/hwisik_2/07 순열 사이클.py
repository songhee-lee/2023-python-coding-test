from collections import deque
import sys

def bfs(start):
    queue = deque([start])
    visited[start] = 1
        
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if nxt == start:
                return 1
            if not visited[nxt]:
                visited[nxt] = 1
                queue.append(nxt)
    return 0    
   
t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
    permu = list(map(int, sys.stdin.readline().rstrip().split()))
    
    graph = [[] * (n + 1) for _ in range(n + 1)] # 문제의 조건 : 1-index
    visited = [0] * (n + 1) # 방문 표시
    
    for i in range(1, n + 1):
        graph[i].append(permu[i - 1]) # permu : 0-index
    
    cycle_count = 0
    for start in range(1, n + 1):
        if not visited[start]:
            cycle_count += bfs(start)
        
    print(cycle_count)
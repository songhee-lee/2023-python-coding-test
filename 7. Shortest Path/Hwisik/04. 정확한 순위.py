# 다시 풀기

import heapq, sys, pprint
INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0
    
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


ret = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    
    if count == n:
       ret += 1
       
print(ret) 

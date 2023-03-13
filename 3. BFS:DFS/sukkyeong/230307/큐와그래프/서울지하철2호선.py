import sys
N = int(input())
parent = [0]*(N+1)
ans = [0]*(N+1)
graph = [[] for _ in range(N+1)]
graphSize = [0]*(N+1)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graphSize[a] += 1
    graphSize[b] += 1
while 1 in graphSize:
    for i in range(1, N+1):
        if graphSize[i] == 1:
            parent[i] = graph[i][0]
            graphSize[i] = 0
            graphSize[parent[i]] -= 1
            graph[parent[i]].remove(i)
while any(parent):
    for i in range(1, N+1):
        if parent[i] != 0:
            if parent[parent[i]] == 0:
                ans[i] = ans[parent[i]]+1
                parent[i] = 0
for i in range(1, N+1):
    print(ans[i], end=' ')

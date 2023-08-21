from collections import deque

def dfs(graph, v, visited):
    visited[v] = False   # 방문 처리
    print(v, end=' ')

    for i in range(1, N+1):
        if graph[v][i] and visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = False

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(1, N+1):
            if graph[v][i] and visited[i]:
                queue.append(i)
                visited[i] = False

# 1. 입력 받기
N, M, V = map(int, input().split())
graph = [ [False] * (N+1) for _ in range(N+1) ]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

visited = [True] * (N+1)    # 방문했는지 확인

# 2. DFS & BFS
dfs(graph, V, visited[:])
print("")
bfs(graph, V, visited[:])
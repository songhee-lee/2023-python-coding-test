N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def dfs(start, graph, visited) :
    for i in range(N) :
        if graph[start][i] and not visited[i]:
            visited[i] = True
            dfs(i, graph, visited)

    return [1 if visited[i] else 0 for i in range(N)]

for node in range(N):
    graph[node] = dfs(node, graph, [False]*N)

for i in range(N):
    print(*graph[i])
'''
- 방향 없는 그래프
- 모든 정점에 대해 DFS를 수행한다.
- 현재 노드와 연결된 모든 노드에 대해서 DFS 재귀 호출.
- 방문한 노드는 표시를 해준다.

'''
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS
def dfs(cur):
    visited[cur] = 1
    
    for nxt in graph[cur]:
        if not visited[nxt]: # 방문하지 않았을 때
            dfs(nxt)

connected_component_cnt = 0 # 연결 요소 개수

for cur in range(1, n + 1):
    if not visited[cur]:
        dfs(cur) # DFS
        connected_component_cnt += 1 # 연결 요소 개수 + 1

# 출력
print(connected_component_cnt)
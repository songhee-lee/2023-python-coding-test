INF = int(1e9)

n,m = map(int,input().split()) # 노드 개수, 간선 개수


graph = [[INF] * (n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

# 자기 자신 -> 비용 0
for a in range(1, n+1):
    for b in range(1,n+1):
        if a==b: graph[a][b]=0

# 간선 초기화
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x,k = map(int,input().split())

# 플로이드 워셜
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

distance= graph[1][k]+graph[k][x]

if distance>=INF : print(-1)
else: print(distance)
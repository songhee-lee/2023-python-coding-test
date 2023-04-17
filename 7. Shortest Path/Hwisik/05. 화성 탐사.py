import sys, heapq

# 개선된 다익스트라 알고리즘
def dijkstra(x, y):
    q = []
    heapq.heappush(q, (graph[x][y], x, y))
    dist[x][y] = graph[x][y]
    
    while q:
        d, x, y = heapq.heappop(q)
        
        if dist[x][y] < d:
            continue
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n: # 범위 내에 있으면
                cost = d + graph[nx][ny]
                
                if cost < dist[nx][ny]: # 최단 거리 갱신
                    dist[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))


INF = int(1e9)
# 방향 정보(상, 하, 좌, 우)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]
    
    dijkstra(0, 0)
    
    print(dist[n - 1][n - 1])
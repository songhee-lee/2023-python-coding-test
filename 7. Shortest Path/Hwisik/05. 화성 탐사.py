import sys, heapq

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
            
            if 0 <= nx < n and 0 <= ny < n:
                cost = d + graph[nx][ny]
                
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))


INF = int(1e9)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]
    
    dijkstra(0, 0)
    print(dist)
    print(dist[n - 1][n - 1])
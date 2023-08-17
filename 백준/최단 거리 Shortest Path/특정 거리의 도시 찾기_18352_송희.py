from collections import deque

N, M, K, X = map(int, input().split())
roads = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b = map(int, input().split())
    roads[a].append(b)

visited = [False] * (N+1)
visited[X] = True
q = deque([([X], 0)])

while q :
    cities, dist = q.popleft()

    if dist == K :
        if cities :
            for city in sorted(cities) :
                print(city)
        else :
            print("-1")
        break

    nxt_cities = []
    for city in cities :
        for nxt in roads[city] :
            if not visited[nxt] :
                nxt_cities.append(nxt)
                visited[nxt] = True
    q.append((nxt_cities, dist+1))
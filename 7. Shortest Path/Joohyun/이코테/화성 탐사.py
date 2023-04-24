import heapq
from sys import stdin
input = stdin.readline
INF = int(1e9)

move = [(-1,0), (1,0), (0,-1), (0,1)]

for _ in range(int(input())):
    n = int(input())
    graph=[]
    for __ in range(n):
        graph.append(list(map(int,input().split())))
    
    distance = [[INF]*(n) for ___ in range(n)]

    distance[0][0] = graph[0][0]
    q = []
    q.append((distance[0][0],0,0))

    while q:
        dist,x,y = heapq.heappop(q)

        if dist > distance[x][y]: continue

        for dx,dy in move:
            nx,ny = x+dx, y+dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n : continue

            cost = dist+graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny]=cost
                heapq.heappush(q,(cost,nx,ny))

    print(distance[n-1][n-1])
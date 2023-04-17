"""  
(0,0) -> (N-1, N-1) 로 가는 최소 비용 출력하기
"""
import sys
import heapq
sys = sys.stdin.readline
INF = int(1e9)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

for _ in range(int(input())):   # test case 만큼 반복
    N = int(input())        # 노드 개수

    # 전체 맵 입력 받기
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    distance = [INF]*(N+1)  # 최단 거리 테이블

    x, y = 0, 0     # 시작 위치
    q = [(maps[x][y], x, y)]    # 비용, (시작위치)
    distance[x][y] = maps[x][y]
    while q:
        dist, x, y = heapq.heappop(q)
        if dist[x][y] < dist :
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N :
                continue
            cost = dist + maps[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

print(distance[N-1][N-1])
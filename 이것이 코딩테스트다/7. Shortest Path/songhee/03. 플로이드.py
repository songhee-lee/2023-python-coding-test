""" 
A -> B 최소 비용
"""
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

# 그래프 초기화
graph = [[INF]*(N+1) for _ in range(N+1)]
for a in range(1, N+1):
    graph[a][a] = 0

# 그래프 입력
for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

# 플로드 워셜
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 갈 수 없는 경우 0으로 치환
for a in range(1, N+1):
    for b in range(1, N+1):
        print(0, end=' ') if graph[a][b] == INF else print(graph[a][b], end=' ')
    print()
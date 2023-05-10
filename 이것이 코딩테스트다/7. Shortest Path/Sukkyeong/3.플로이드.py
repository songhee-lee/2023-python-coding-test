'''
n(2 ≤ n ≤ 100)개의 도시가 있다.
그리고 한 도시에서 출발하여 다른 도시에 도착하는
m(1 ≤ m ≤ 100,000)개의 버스가 있다.
각 버스는 한 번 사용할 때 필요한 비용이 있다.
모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데
필요한 비용의 최솟값
'''

import sys

# 무한을 의미하는 값으로 10억을 설정
INF = int(1e9)

# 도시의 개수
n = int(input())

# 도시간의 버스 노선 정보를 입력받아 2차원 리스트로 저장
graph = [[INF] * (n + 1) for _ in range(n + 1)]
m = int(input())  # 버스 노선의 개수
for _ in range(m):
    a, b, c = map(int, input().split())
    # 동일한 도시간의 버스 노선이 여러 개인 경우 최소값으로 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 자기 자신으로 가는 버스 노선은 0으로 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

# 플로이드-와샬 알고리즘 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

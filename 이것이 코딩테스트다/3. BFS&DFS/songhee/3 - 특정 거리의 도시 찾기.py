""" 
https://www.acmicpc.net/problem/18352

1. 입력 받기
    - 도시 개수  N, 도로 개수 M, 거리 정보 K, 출발 도시의 번호 X
    - 단방향 도로 정보 
2. 최단 거리 초기화
3. 최단 경로 구하기 (X로부터 K거리)
4. 출력
    - X로부터 출발할 수 있는 도시 중, 최단 거리가 K인 모든 도시 번호 출력하기 없으면 -1 출력하기

*** 시간초과
sys.stdin.readline().rstrip().split() 사용하기

"""

from collections import deque
import sys

# 1. 입력 받기
N, M, K, X = map(int, input().split())

roadway = [ [] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())  # 시간 초과를 위한 부분
    roadway[a].append(b)

# 2. 최단 거리 초기화
distance = [-1] * (N+1)
distance[X] = 0

# 3. 최단 경로 구하기 (X로부터 K거리)
q = deque([X])
while q :
    now = q.popleft()

    # 현재 도시에서 이동 가능한 모든 도시 확인
    for next in roadway[now]:
        # 방문 안한 곳이면 최단 거리 갱신
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)
    
# 최단 거리 K인 모든 도시 출력
if K in distance:
    for i in range(1, N+1):
        if distance[i] == K :
            print(i)
else:
    print(-1)
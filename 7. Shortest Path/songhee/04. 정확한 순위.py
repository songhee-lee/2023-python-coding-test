""" 
- 성적 비교 결과가 주어질 때, 정확한 성적 순위를 알 수 있는 학생 수 구하기
- 자신보다 낮은 학생 수 기록하기

- 최단 경로 존재 = 성적 비교 가능
- 성적 비교 가능한 학생이 N명이면 정확한 순위 알 수 있음
"""
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
# 그래프 초기화 및 입력
graph = [[INF]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] =1

# 플로드 워셜
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 순위 비교 가능한 학생 확인
answer = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == N:
        answer += 1

print(answer)
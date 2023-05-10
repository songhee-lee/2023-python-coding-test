""" 
- 2초 / 128MB

- 일부 학생들의 키를 비교한 결과가 주어졌을 때, 키 순서로 줄 세우기

+ 위상 정렬 문제
"""
import sys
from collections import deque

# 1. 입력 받기
N, M = map(int, input().split())    # 학생 수, 비교 횟수
graph = [ [] for _ in range(N+1) ]  # 비교 결과
degree = [ 0 for _ in range(N+1)]   # 진입 차

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)    # b는 a보다 크다
    degree[b] += 1        # b 보다 작은게 1개 추가됨

# 2. 정렬하기
queue = deque() 
result = []         

# 가장 작은 학생 찾기
for i in range(1, N+1):
    if degree[i] == 0:
        queue.append(i)

# 가장 작은 학생부터 정렬 시작
while queue:
    # 현재 학생 추가
    now = queue.popleft()
    result.append(now)

    for j in graph[now]:    # 현재 학생보다 큰 학생
        degree[j] -= 1      
        if degree[j] == 0:  # 그 학생이 다음으로 큰 학생인 경우
            queue.append(j)

print(*result)
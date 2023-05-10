""" 
- 2초 / 256MB

- 
"""
import sys
from collections import deque

# 1. 입력 받기
N = int(input())    # 수행 해야할 작업
graph = [[] for _ in range(N+1)]    # 작업의 선행 관계
time = [ 0 for _ in range(N+1)]     # 작업의 시간
degree = [ 0 for _ in range(N+1)]   # 선행 작업 개수

for i in range(1, N+1):
    line = list(map(int, sys.stdin.readline().split()))

    # 시간, 선행 직업 개수, [선행 관계 작업 번호]
    time[i] = line[0]
    degree[i] = line[1]

    if line[1] == 0:
        continue
    
    graph[i] = line[2:]     # i번 작업을 하기 위한 선행 작업들

# 2. 작업 순서대로 진행
for i in range(1, N+1):
    if graph[i] :
        t = 0
        for j in graph[i]:
            t = max(t, time[j])
        time[i] += t

print(max(time))
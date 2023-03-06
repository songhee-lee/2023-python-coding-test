""" 
- 1초 / 256MB
"""
import sys

def dfs(v):
    # 현재 노드 방문 표시
    visited[v] = False
    now = v

    while True:
        next = numbers[now]
        if visited[next]:
            dfs(next)
        else:
            return

T = int(input())    # 테스트 케이스 개수
for _ in range(T):
    N = int(input())    # 순열 크기
    numbers = list(map(int, sys.stdin.readline().split()))  # 순열
    numbers.insert(0, 0)

    count = 0   # 순열 사이클 개수
    visited = [True]*(N+1)  # 방문 표시
    for i in range(1, N+1):
        if numbers[i] == i:    
            count += 1
            continue

        if visited[i] :
            dfs(i)
            count += 1
    
    print(count)
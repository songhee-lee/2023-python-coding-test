""" 
[ 제한 사항 ]
- 3초 / 512MB

[ 문제 ]
- 방향 없는 그래프 주어졌을 때 연결 요소 개수 구하는 프로그램 작성
- 연결 요소란?
    - 

"""
import sys
sys.setrecursionlimit(10000)

def dfs(v):

    # 현재 노드 방문 처리
    visited[v] = False

    for e in graph[v]:
        if visited[e]:
            dfs(e)

N, M = map(int, input().split())
graph = [ [] for _ in range(N+1)]    # 그래프
for _ in range(M):
    u, v = map(int, input().split())    # 간선 추가
    graph[u].append(v)
    graph[v].append(u)

result = 0
visited = [ True ] * (N+1)
for i in range(1, N+1):
    if visited[i] :
        dfs(i)
        result += 1

print(result)
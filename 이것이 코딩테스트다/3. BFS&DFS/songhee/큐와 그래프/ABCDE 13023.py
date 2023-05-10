""" 
- A-B-C-D-E 친구 관계가 존재하는지 구하기
"""
from collections import deque

def dfs(start, count):
    global flag
    visited[start] = True
    if count == 4:
        flag = True
        return

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, count+1)
            visited[i] = False

N, M = map(int, input().split())
graph = [ [] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    visited = [False] * N
    flag = False
    dfs(i, 0)
    if flag:
        break

if flag:
    print(1)
else:
    print(0)

#입력1 : 노드 개수
#입력2 : 간선 개수
#입력3 : 간선(양방향)

#출력 : start 1번, 연결된 노드 개수
import sys
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    temp1, temp2 = map(int, sys.stdin.readline().split())
    graph[temp1].append(temp2)
    graph[temp2].append(temp1)

visited = []
que = deque()

visited = [1]
que = [1]
while que:
    cur = que.pop(0)
    for i in graph[cur]:
        if i not in visited:
            visited.append(i)
            que.append(i)

print(len(visited)-1)

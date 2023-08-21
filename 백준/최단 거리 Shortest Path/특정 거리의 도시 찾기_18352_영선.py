#입력1 : 노드 n, 간선 m, 최단거리 k, 출발번호 x
#입력2 : a->b 단방향 그래프

#모든 도로 거리 1

#출력 : 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력 / 없으면 -1
import sys
from collections import deque
n, m, k, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    temp1, temp2 = map(int, sys.stdin.readline().split())
    graph[temp1].append(temp2)

dist = [0] * (n+1)
visited = [False] * (n+1) 

answer = []
que = deque([start])
visited[start] = True
dist[start] = 0

while que:
    cur = que.popleft()
    for i in graph[cur]:
        if not visited[i]:
            visited[i] =True
            que.append(i)
            dist[i] = dist[cur] +1
            if dist[i] == k:
                answer.append(i)

if len(answer) == 0:
    print(-1)

else:
    answer.sort()
    for i in answer:
        print(i)

    

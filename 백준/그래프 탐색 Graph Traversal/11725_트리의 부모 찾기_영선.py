#입력1 : N 노드 개수
#입력2 : N-1 줄에 트리 상에서 연결된 두 정점

#출력 : N-1 줄에 각 노드의 부모 노드 번호를 2번 노드부터 출력

#루트는 1, 이진트리가 아닐지도?
import sys
from collections import deque

def bfs(start,visit):
    que = deque([start])
    visit[start] = 1

    while que :
        cur = que.popleft()

        for i in graph[cur]:
            if visit[i] == 0 :
                que.append(i)
                visit[i] = cur
    


n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


visit = [0 for _ in range(n+1)]

bfs(1,visit)

for i in range(2,n+1):
    print(visit[i])
    


#입력1 : N M V 정점 간선 시작
#입력2 : M개의 줄에 연결 (여러개 간선 가능)

#방문 정점이 여러개면 작은 번호부터
#연결된 것이 없어도 그 정점 자체는 출력

#출력1 : DFS 결과
#출력2 : BFS 결과
import sys
from collections import deque

def DFS(cur):
    visited_d[cur] = True
    print(cur, end=" ")
    
    for i in graph[cur]:
        if not visited_d[i]:
            DFS(i)


def BFS(start):
    visited_b[start] = True
    que = deque([start])
    while que:
        cur = que.popleft()
        print(cur, end=" ")
        for i in graph[cur]:
            if not visited_b[i]:
                visited_b[i] = True
                que.append(i)

    

    
if __name__ == "__main__":
    n, m, v = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        temp1, temp2 = map(int, sys.stdin.readline().split())
        graph[temp1].append(temp2)
        graph[temp2].append(temp1)
        
    for i in range(1,n+1):
        graph[i].sort()
        
    #dfs
    visited_d =[False] * (n+1)
    DFS(v)
    print()
    #bfs
    visited_b =[False] * (n+1)
    BFS(v)

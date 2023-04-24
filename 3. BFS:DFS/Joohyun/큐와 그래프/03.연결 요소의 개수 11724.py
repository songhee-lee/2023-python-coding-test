"""
>> 무방향 그래프의 연결 요소의 개수 구하기 <<

< 입력 >
n : 정점의 개수 ( 1 <= n <= 1,000 )
m : 간선의 개수 ( 0 <= m <= nx(n-1)/2 )
간선의 양 끝점 u, v ( 1<= u,v <= n , u!=v )

< 출력 >
연결 요소의 개수
"""


"""
< FLOW : DFS >
1. 인접 리스트 만들기
2. 연결 요소 개수 구하기 : DFS
    완전 탐색 : 인접 리스트 차례대로
    1) 리스트가 비어있으면, PASS
    2) 리스트가 안비어있으면, DFS (vertex 1개)
        pop -> 재귀
    3)  DFS 끝나면 연결 요소 +1

< FLOW : BFS >
1. 인접 리스트 만들기
2. 연결 요소 개수 구하기 : BFS
    완전 탐색 : 인접 리스트 차례대로
    1) 리스트가 비어있으면, PASS
    2) 리스트가 안비어있으면, BFS(리스트)
        1. 리스트 모든 요소를 큐에 삽입 : (v1,v2)
        2. 큐가 빌 때까지
            그래프[v1].remove(v2)
            그래프[v2].remove(v1)
            그래프[v2]의 모든 요소 큐에 삽입

< FLOW : 인접 행렬 >
1. 방문 여부 : [[False]*n]
2. 간선 하나씩 뽑아서 확인
    (v1,v2) ->
    남은 간선 전체 확인 : v1 in 간선s -> 삭제
"""
from sys import stdin
from collections import deque

# 연결 요소 구하기
def bfs(g):
    q = deque()
    for v1,v2 in g:q.append((v1,v2))
    while q:
        v1, v2 = q.popleft()
        graph[v1].remove((v1,v2))
        graph[v2].remove((v2,v1))

        for v1,v2 in graph[v2] :
            if not (v2,v1) in q :
                if not (v1,v2) in q: 
                    q.append((v1,v2))

input = stdin.readline

n,m=map(int,input().split())    # n : 정점개수 , m : 간선 개수
edges = [[]*(n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    edges[i].append(j)
#edges = [list(map(int,input().split())) for _ in range(m)]
#visited = [[True] *(n+1)]   # 방문여부

# 1. Adjacency List 만들기
#graph = [[] for _ in range(n+1)]
#for v1,v2 in edges:
    #graph[v1].append(v2)

# 2. 연결 요소 개수 구하기
cnt = 0 # 연결 요소 개수
q=deque()
for i in range(1,n+1):
    if edges[i]:
        q.append(i)
        while q:
            q.append(edges[i])
            edges[i]=0
        cnt+=1



        # if visited[i]:
        #     visited[i]=False
        #     bfs(graph[i])
        #     cnt+=1

print(cnt)
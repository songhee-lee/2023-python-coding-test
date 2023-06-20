import sys
sys.setrecursionlimit(10**6)
answer = 0

def dfs(now, parent, graph, a) :
        global answer
        # 현재 노드 now의 자식노드로 이동 (depth 우선 탐색)
        for c in graph[now] :
            if c != parent :
                dfs(c, now, graph, a)
        # 현재 노드 0으로 만들기
        a[parent] += a[now]
        answer += abs(a[now])

def solution(a, edges):
    if sum(a) != 0 :            # 0으로 만들 수 없는 경우
        return -1

    n = len(a)
    # 그래프 만들기
    graph = [[] for _ in range(n)]
    for s, e in edges :
        graph[s].append(e)
        graph[e].append(s)
        
    dfs(0, 0, graph, a)      
    return answer

import sys
sys.setrecursionlimit(10 ** 6)

def solution(n, lighthouse):
    graph = [[] for _ in range(n + 1)] # 양방향 그래프
    check = [0] * (n + 1) # 방문 처리
    
    # 양방향 그래프 만들기
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    
    # DFS
    def dfs(x):
        check[x] = 1 # 방문처리
        
        # 리프 노드라면
        if not graph[x]:
            return 1, 0 # on, off
        
        # 리프 노드가 아니라면
        # 방문하지 않은 자식 노드를 리스트로 만든다.
        child = [nxt for nxt in graph[x] if not check[nxt]]
        
        # 점등, 소등
        on, off = 1, 0
        
        # 자식노드를 탐색하면서
        for c in child:
            c_on, c_off = dfs(c) # 해당 자식노드를 켜거나 끌 경우
            on += min(c_on, c_off) # 나(특정 노드)를 켤 경우
            off += c_on # 나(특정 노드)를 끌 경우 자식은 반드시 켜야한다.
        
        return on, off
    
    # 뱃길은 모두 이어져있으므로 시작 노드는 상관이 없다.
    on, off = dfs(1)
    
    return min(on, off) # 최소로 켜는 등대 개수를 반환한다.
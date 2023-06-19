_max = 1
def solution(info, edges):
    graph = [[] for _ in range(len(info))] # 연결 정보
    
    # 연결 정보 초기화
    for p, c in edges:
        graph[p].append(c)
    
    # DFS
    # 현재 정점, 양의 수, 늑대의 수, 이동 가능한 정점 리스트
    def dfs(p, sheep, wolf, node_list):
        global _max
        # 양의 수가 더 많으면
        if sheep > wolf:
            _max = max(_max, sheep) # 최대 양의 수 갱신
        else: # 늑대의 수가 더 많으면
            return
        
        # 이동 가능한 정점 리스트 갱신
        node_list.extend(graph[p])
        
        for node in node_list:
            # 자기 자신이 아닌 정점 리스트로 호출
            if info[node] == 0: # 양이라면
                dfs(node, sheep + 1, wolf, [i for i in node_list if i != node])
            else: # 늑대라면
                dfs(node, sheep, wolf + 1, [i for i in node_list if i != node])
    
    # DFS 호출
    dfs(0, 1, 0, [])    
    
    return _max
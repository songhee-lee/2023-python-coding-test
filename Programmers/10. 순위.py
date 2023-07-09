def solution(n, results):
    rank = [[0] * n for _ in range(n)]
    
    # 1: 왼쪽이 오른쪽을 이겼다.
    # -1: 왼쪽이 오른쪽한테 졌다.
    # results는 1-index
    for a, b in results:
        rank[a - 1][b - 1] = 1 
        rank[b - 1][a - 1] = -1
        
    
    for k in range(n): # 경유점
        for i in range(n): # 시작점
            for j in range(n): # 끝점
                if i == j:
                    continue
                
                # i가 k를 이기고, k가 j를 이겼다 : i가 j를 이겼다.
                if rank[i][k] == rank[k][j] == 1:
                    rank[i][j] = 1 # 이겼음을 표시
                    rank[j][i] = rank[j][k] = rank[k][i] = -1 # 졌음을 표시. (not 이겼음 = 졌음)
    
    can_be_ranked = 0
    
    # 정확한 순위를 매길 수 있는지 확인하기
    for r in rank:
        if r.count(0) == 1:
            can_be_ranked += 1
            
    return can_be_ranked
def solution(alp, cop, problems):
    # 최대 알고력, 코딩력
    max_alp, max_cop = 0, 0
    
    # 최대 알고력, 코딩력 구하기
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])
    
    # dp[now_alp][now_cop] = 알고력 = now_alp, 코딩력 = j에 도달하기 위해 걸리는 시간
    dp = [[float('inf') for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    
    # 목표 알고력, 코딩력
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    # 이미 현재 알고력, 코딩력이므로... 걸린 시간이 0이다.
    dp[alp][cop] = 0 
    
    for now_alp in range(alp, max_alp + 1):
        for now_cop in range(cop, max_cop + 1):
            # 알고리즘, 코딩 공부(1의 시간이 흐른다)
            if now_alp < max_alp:
                dp[now_alp + 1][now_cop] = min(dp[now_alp + 1][now_cop], dp[now_alp][now_cop] + 1)
            if now_cop < max_cop:
                dp[now_alp][now_cop + 1] = min(dp[now_alp][now_cop + 1], dp[now_alp][now_cop] + 1)
                
            # 문제를 풀어서 알고력, 코딩력 높이기
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if now_alp >= alp_req and now_cop >= cop_req:
                    nxt_alp = min(now_alp + alp_rwd, max_alp)
                    nxt_cop = min(now_cop + cop_rwd, max_cop)
                    dp[nxt_alp][nxt_cop] = min(dp[nxt_alp][nxt_cop], dp[now_alp][now_cop] + cost)
                    
    return dp[-1][-1]
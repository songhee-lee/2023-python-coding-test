""" 
- 알고력 -> 알고리즘 공부 1시간 +1
- 코딩력 -> 코딩 공부 1시간 +1

- 주어진 모든 문제를 풀 수 있는 알고력과 코딩력 얻는 최단시간
    -> 모든 문제를 풀 필요는 없음
    
- 최대치 알고력, 코딩력 구하기
- 최대치 도달할 때까지 현재 풀 수 있는 문제 중에 가장 reward 높은 것 구하기 (cost 낮고)
- 같은 문제 여러번 풀 수 있음
"""

def solution(alp, cop, problems):
    
    # 필요한 최대 알고력, 코딩력
    max_alp = max_cop = 0
    for a, c, *_ in problems:
        max_alp = max(a, max_alp)
        max_cop = max(c, max_cop)
    
    # DP[alp][cop] : alp & cop 도달하는데 걸리는 최단 시간
    INF = float('inf')
    dp = [ [INF]*(151) for _ in range(151)]
    
    alp, cop = min(alp, max_alp), min(cop, max_cop)
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            # 1시간 공부한 경우 check
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            
            # 모든 문제 중 풀 수 있는 것 확인
            for a, c, alp_rwd, cop_rwd, cost in problems:
                if i >= a and j >= c:
                    # 풀어서 얻는 알고력, 코딩력 업데이트
                    next_alp = min(max_alp, i + alp_rwd)
                    next_cop = min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
                
    return dp[max_alp][max_cop]
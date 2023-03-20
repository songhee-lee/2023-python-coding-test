"""
DP 배열을 정의하면 문제에서 요구하는 답은 dp[목표 알고력][목표 코딩력]입니다.
dp[초기 알고력][초기 코딩력] = 0으로 기저 사례를 잡고 나머지 DP 배열의 값은 무한(적당히 큰 값)으로 초기화한 후 다음과 같은 방법으로 DP 배열을 업데이트 합니다.

알고리즘을 공부하여 알고력을 1 높이는 경우:
dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
코딩을 공부하여 코딩력을 1 높이는 경우:
dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
문제 하나를 선택하여 알고력과 코딩력을 높이는 경우:
dp[i+alp_rwd][j+cop_rwd] = min(dp[i+alp_rwd][j+cop_rwd], dp[i][j]+cost) (단, i >= alp_req이고 j >= cop_req)

초기 알고력 <= i <= 목표 알고력, 초기 코딩력 <= j <= 목표 코딩력인 모든 (i, j)에 대해서 dp[i][j] 값을 업데이트해야 하므로, 시간 복잡도는 O(목표 알고력 * 목표 코딩력 * (problems 배열의 길이))가 됩니다.

이 방법 이외에도, 그래프로 모델링하여 최단 거리를 찾는 문제(다익스트라 알고리즘 사용)로 바꾸어 해결하는 풀이도 있습니다.
"""


def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    time = 0
    for a, b, c, d, e in problems:
        max_alp = max(max_alp, a)
        max_cop = max(max_cop, b)
        time += e
    # 목표 알고력
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    INF = float('inf')
    dp = [[INF]*(max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp, next_cop = min(
                        max_alp, i + alp_rwd), min(max_cop, j + cop_rwd)
                    dp[next_alp][next_cop] = min(
                        dp[next_alp][next_cop], dp[i][j] + cost)
    return dp[-1][-1]

'''
[문제]
- N * M 크기의 초콜릿. 초콜릿은 금이 가 있는 모양이다.
- 초콜릿을 쪼개서 총 N * M개의 조각으로 쪼개려고 한다.
- 초콜릿을 쪼개는 횟수를 최소로 하려고 한다. 초콜릿의 크기가 주어졌을 때, 이를 1 * 1 크기의 초콜릿으로 쪼개기 위한 최소 쪼개기 횟수를 구하라.

[점화식]
- dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j] + 1) (1 <= k <= i // 2)
                min(dp[i][j], dp[i][k] + dp[i][j - k] + 1) (1 <= k <= j // 2)
    -> 가로가 i이고 세로가 j인 초콜릿을 쪼갤 때, 가로로 쪼개는 경우
    -> 세로가 j이고 가로가 i인 초콜릿을 쪼갤 때, 세로로 쪼개는 경우

-> DP의 문제점은 가로, 세로에 상관없이 같은 값이 나온다는 것이다.
    예를 들어 2 * 4짜리는 4 * 2 짜리와 같다. 왜냐? 초콜릿 회전하면 그만이니까.
    근데 DP는 2중 for문을 사용해서 오래걸린다.

-> 수학적 풀이를 하자! n * m - 1이 답이다.

'''

n, m = map(int, input().split())

# DP 풀이
def dp_helper():    
    # dp 테이블 초기화(행 : 가로, 열 : 세로)
    dp = [[float('inf') for _ in range(301)] for _ in range(301)]

    # 가로가 1일 때
    for i in range(1, n + 1):
        dp[i][1] = i - 1
        
    # 세로가 1일 때
    for i in range(1, m + 1):
        dp[1][i] = i - 1

    # 2 * 2 ~ n * m까지
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            
            # 가로로 쪼개기
            # 1 ~ i // 2까지(전체를 비교할 필요 없음, 절반까지만 비교해도 똑같다.)
            for k in range(1, i // 2 + 1):
                dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j] + 1)
                
            # 세로로 쪼개기
            # 1 ~ j // 2까지(전체를 비교할 필요 없음, 절반까지만 비교해도 똑같다.)
            for k in range(1, j // 2 + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j - k] + 1)
                
    print(dp[n][m])

# 수학적 풀이
def math_helper():
    print(n * m - 1)

math_helper()
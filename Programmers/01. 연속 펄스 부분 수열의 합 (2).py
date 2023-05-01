def solution(sequence):
    N = len(sequence)
    # dp 테이블
    dp = [[0] * N for _ in range(2)]
    # dp 테이블 초기화 
    dp[0][0] = sequence[0]          # 짝수일 때 +
    dp[1][0] = sequence[0] * -1     # 짝수일 때 -

    for i in range(1, N):
        # i번째로 새로운 구간 시작 vs (이전까지 구간합 + 현재 값)
        dp[0][i] = max(sequence[i], dp[1][i-1] + sequence[i])
        dp[1][i] = max(-sequence[i], dp[0][i-1] - sequence[i])

    return max(max(dp[0]), max(dp[1]))

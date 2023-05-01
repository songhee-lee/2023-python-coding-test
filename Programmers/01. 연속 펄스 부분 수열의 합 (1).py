import sys

def solution(sequence):
    n = len(sequence)   # sequence 길이

    # dp 테이블
    dp = [[[-sys.maxsize]*2 for _ in range(2)] for _ in range(n)]
    # dp 테이블 초기화 - 자기 자신일 때를 최댓값으로 설정
    for i in range(n):
        flag = 1 if i % 2 else -1       # flag : 홀수면 1 짝수면 -1

        dp[i][1][0] = sequence[i] * (-flag) # 짝수 부호가 +
        dp[i][1][1] = sequence[i] * flag    # 홀수 부호가 +

    for i in range(1, n):
        # i 번째를 포함하지 않을 때 최댓값
        dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][1][0])
        dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][1][1])     
        # i 번째를 포함할 때 최댓값
        flag = 1 if i % 2 else -1       # flag : 홀수면 1 짝수면 -1
        dp[i][1][0] = max(dp[i][1][0], dp[i-1][1][0] + sequence[i] * (-flag))
        dp[i][1][1] = max(dp[i][1][1], dp[i-1][1][1] + sequence[i] * flag)
    
    return max(dp[n-1][0][0], dp[n-1][0][1], dp[n-1][1][0], dp[n-1][1][1])

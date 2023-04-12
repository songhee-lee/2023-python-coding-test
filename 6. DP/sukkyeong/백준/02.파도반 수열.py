T = int(input())  # 테스트 케이스 개수 입력

for _ in range(T):
    N = int(input())  # 자연수 N 입력
    dp = [0] * 101  # dp 리스트 초기화

    # 초기값 설정
    dp[1], dp[2], dp[3] = 1, 1, 1
    dp[4], dp[5] = 2, 2

    # DP 계산
    for i in range(6, N+1):
        dp[i] = dp[i-1] + dp[i-5]

    print(dp[N])  # P(N) 출력

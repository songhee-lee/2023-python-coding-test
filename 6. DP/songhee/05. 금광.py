""" 
- NxM 크기의 금광
- 첫 번째 열에서 출발
- M번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래 위치로 이동
- 채굴 가능한 금의 최대 크기
"""

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    golds = list(map(int, input().split()))

    # dp[i][j] : i번째 행에서 j번째 움직일 때 채굴 가능한 금 최대 크기
    dp = [[0] * M for _ in range(N) ]
    for i in range(N):
        dp[i][0] = golds[i*M]

    print(dp)

    # Bottom-up
    for j in range(1, M):
        for i in range(N):
            if i == 0 :
                # 오른쪽 vs 아래서 위로
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1])
            elif i == N-1:
                # 위에서 아래 vs 오른쪽
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

            dp[i][j] += golds[i*M+j]

    print(dp)
    answer = max([ line[-1] for line in dp ])
    print(answer)
""" 
- 스티커를 떼면 변을 공유하는 스티커는 사용할 수 없다
- 점수의 합이 최대가 되도록 스티커 뜯기
"""

T = int(input())
for _ in range(T):
    N = int(input())
    stickers = [ list(map(int, input().split())) for _ in range(2) ]

    # dp[x][0] : x번째 열 포함하지 않을 때 최대 점수
    # dp[x][1] : x번째 열 1행 뜯을 때 최대 점수
    # dp[x][2] : x번째 열 2행 뜯을 때 최대 점수
    dp = [[0]*3 for _ in range(N)]
    dp[0][1] = stickers[0][0]
    dp[0][2] = stickers[1][0]
    
    # Bottom-up
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + stickers[0][i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + stickers[1][i]

    print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

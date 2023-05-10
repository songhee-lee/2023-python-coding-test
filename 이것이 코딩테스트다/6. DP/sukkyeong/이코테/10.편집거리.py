'''
최소 편집 거리를 담을 이차원 배열을 초기화
최소 편집 거리를 계산해 테이블에 저장

행과 열에 해당하는 문자가 서로 같으면, 왼쪽 위에 해당하는 수를 대입
행과 열에 해당하느 문자가 다르면, 왼쪽, 위쪽, 왼쪽 위에 해당하는 수 중에서
가장 작은 수에 1을 더해 대입
'''


def solution(str1, str2):
    n = len(str1)
    m = len(str2)
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[[i-1][j-1]])
        return dp[n][m]
    str1 = input()
    str2 = input()

    print(solution(str1, str2))

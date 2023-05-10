'''
아이돌 그룹 결성

'''

s, a, b, c = map(int, input().split())

dp = [[[[-1 for _ in range(51)] for _ in range(51)]
       for _ in range(51)] for _ in range(51)]


def go(n, a, b, c):
    if n == 0:
        if a == 0 and b == 0 and c == 0:
            return 1
        else:
            return 0
    if a < 0 or b < 0 or c < 0:
        return 0
    if dp[n][a][b][c] != -1:
        return dp[n][a][b][c]
    dp[n][a][b][c] = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if i + j + k == 0:
                    continue
                dp[n][a][b][c] += go(n - 1, a - i, b - j, c - k)
    dp[n][a][b][c] %= 1000000007
    return dp[n][a][b][c]


print(go(s, a, b, c))

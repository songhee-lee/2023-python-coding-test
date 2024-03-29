'''
[문제]
- 어떤 자연수는 그보다 작은 제곱수들의 합으로 표현할 수 있다.
- 예를 들어 11 = 3^2 + 1^2 + 1^2 = 2^2 + 2^2 + 1^2 + 1^2이다.
- 이때 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.
- 주어진 자연수 N을 그 합으로써 표현할 수 있는 '제곱수 항의 최소 개수'를 구하는 프로그램을 작성하시오.

[점화식]
- dp[i] 는 i로 초기화 한다.
- dp[i] = min(dp[i], dp[i - j ** 2] + 1)
    -> 숫자 i를 i보다 작은 제곱수들의 합으로 표현할 때 제곱수 항의 최소 개수

ex) dp[4] = min(dp[4 - 1 ** 2] + 1, dp[4 - 2 ** 2] + 1, dp[4])
    (참고. dp[3] = 3, dp[0] = 0)
    -> dp[4] = 2^2 or 1^2 + 1^2 + 1^2 + 1^2 -> 최소는 2^2
'''

n = int(input())

# dp 테이블 (n + 1)개로 초기화
dp = [float('inf')] * (n + 1)
dp[0] = 0
dp[1] = 1

# 점화식
for i in range(2, n + 1):
    # 모든 수의 제곱수 항은 '1의 제곱 * 자기 자신'을 개수로 가지므로, i로 초기화
    dp[i] = i
    # j는 제곱수
    for j in range(1, i):
        # 제곱수가 i보다 크다면, 더 이상 탐색할 필요가 없다.
        if j ** 2 > i:
            break
        # 제곱수가 i보다 작다면, dp[i]를 갱신한다.
        dp[i] = min(dp[i], dp[i - j ** 2] + 1)

print(dp[n])
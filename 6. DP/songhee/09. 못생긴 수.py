""" 
- 1은 못생긴 수
- 2, 3, 5 만을 소인수로 가지는 수

- N번째 못생긴 수 찾기
"""

N = int(input())

# dp[x] : x번째 못생긴 수
dp = [0] * (N+1)
dp[1] = 1

# Bottom-up
i2 = i3 = i5 = 1         # 곱셈 인덱스
n2, n3, n5 = 2, 3, 5     # 다음 숫자 후보
for i in range(2, N+1):
    dp[i] = min( n2, n3, n5)

    if dp[i] == n2:
        i2 += 1
        n2 = dp[i2] * 2
    if dp[i] == n3:
        i3 += 1
        n3 = dp[i3] * 3
    if dp[i] == n5:
        i5 += 1
        n5 = dp[i5] * 5

print(dp[N])



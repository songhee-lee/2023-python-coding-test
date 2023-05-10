"""
 - 어떤 암호가 주어졌을 때 해석이 몇 가지 나올 수 있는지 구하기
"""

cipher = list(map(int, input()))
n = len(cipher)

# 예외 - 암호가 잘못된 경우
if n == 0 or cipher[0] == 0 :
    print(0)
    exit(0)

mod = 1000000
# dp[x] : x 번째까지의 암호 개수
dp = [0] * (n+1)
dp[0] = dp[1] = 1
cipher = [0] + cipher

for i in range(2, n+1):
    now, prev = cipher[i], cipher[i-1]
    if 1 <= now <= 9:
        dp[i] += dp[i-1]
    # 해석 불가능한 경우
    elif prev == 0 or prev >= 3:
        print(0)
        exit(0)

    prev = prev*10 + now
    if 10 <= prev <= 26:
        dp[i] += dp[i-2]    
    dp[i] %= mod

print(dp[n] % mod)
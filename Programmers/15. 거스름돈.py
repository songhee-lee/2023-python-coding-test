# 거슬러 줄 방법의 수 구하기.
# 거스름돈을 먼저 설정하면 실패한다.
# 동전의 종류를 먼저 설정해야 한다.
MOD = 1000000007
def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    # 성공 코드 - 동전의 종류 먼저 설정하기
    for m in money:
        for i in range(m, n + 1):
            dp[i] += dp[i - m] % MOD
    
    # 실패 코드 - 거스름돈을 먼저 설정하기
    # for i in range(1, n + 1):
    #     for m in money:
    #         dp[i] += dp[i - m] % MOD
    
    return dp[n]
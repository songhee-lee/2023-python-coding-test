"""
동전 종류 : n개
동전으로 k원 만들기, 동전 개수 제한 없음
동전 구성 가타고, 순서 다르면 같은 경우의 수
"""
n,k=map(int,input().split())
coins = sorted([int(input()) for _ in range(n)])
dp = [0]*(k+1)
dp[0]=1 # 코인 1개로 만들 수 있는 경우의 수를 위한 초기화

for coin in coins:
    for coin_sum in range(coin,k+1):
        if coin_sum-coin >= 0: dp[coin_sum]+=dp[coin_sum-coin]

print(dp[k])
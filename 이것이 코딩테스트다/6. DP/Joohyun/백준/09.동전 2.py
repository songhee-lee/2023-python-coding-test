n,k = map(int,input().split())
coins = sorted([int(input()) for _ in range(n)])
dp=[10001] * (k+1)
dp[0]=0
for coin in coins:
    for coin_sum in range(coin,k+1):
        if coin_sum-coin >= 0 : 
            dp[coin_sum]=min(dp[coin_sum], dp[coin_sum-coin]+1)
if dp[k]==10001 : print(-1)
else: print(dp[k])



# 메모리 초과
# n,k = map(int,input().split())
# coins = sorted([int(input()) for _ in range(n)])
# dp=[[]*n for _ in range(k+1)]
# for coin in coins:
#     for coin_sum in range(coin,k+1):
#         if coin_sum-coin >= 0 : 
#             if len(dp[coin_sum-coin]) :
#                 for coin_num in dp[coin_sum-coin]:
#                     dp[coin_sum].append(coin_num+1)
#             else : dp[coin_sum].append(1)

# print(min(dp[k]))






# 메모리 초과
# n,k = map(int,input().split())
# coins = sorted([int(input()) for _ in range(n)])
# dp=[[]*n for _ in range(k+1)]
# for coin in coins:
#     for coin_sum in range(coin,k+1):
#         if coin_sum-coin >= 0 : 
#             if dp[coin_sum-coin] :
#                 for before_sum in dp[coin_sum-coin]:
#                     dp[coin_sum].append(before_sum+[coin])
#             else : dp[coin_sum].append([coin])


# min_len = k
# for k_sum in dp[k]:
#     min_len=min(min_len,len(k_sum))
# print(min_len)

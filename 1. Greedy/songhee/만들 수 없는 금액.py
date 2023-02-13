"""Pseudo Code

1. 입력 받고 배열에 저장
2. 모든 조합의 수 계산
3. 만들 수 없는 가장 작은 수 찾기

"""

from itertools import combinations

# 1. 입력 받기
N = int(input())
coins = list(map(int, input().split()))

# 2. 모든 조합의 수 계산
coins_comb = []
for i in range(1, len(coins)):    # 동전 1개 ~ N개 합까지
    coins_comb += [sum(x) for x in list(combinations(coins, i))]

coins_comb = set(coins_comb)

# 3. 만들 수 없는 가장 작은 수 찾기
result = 1
for i in coins_comb:
    if result < i :
        break
    
    result += 1

print(result)

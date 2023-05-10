""" 
- N개 수 중 어떤 수가 다른 두 수의 합으로 나타낼 수 있으면 GOOD
"""

N = int(input())
numbers = list(map(int, input().split()))

# 두 수의 합 구하기
goods = {}
for i in range(N):
    for j in range(i+1, N):
        x = numbers[i]+numbers[j]
        if x in goods:
            goods[x].append((i, j))
        else:
            goods[x] = [(i, j)]

# 두 수의 합으로 나타낼 수 있는지 확인
cnt = 0
for k, n in enumerate(numbers):
    if n in goods:  # 나타낼 수 있고
        for x, y in goods[n]: # 서로 다른 두 수인 경우
            if x != k and y != k:
                cnt += 1
                break

print(cnt)
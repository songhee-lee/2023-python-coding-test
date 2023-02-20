
N = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for x in coins:
    #만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
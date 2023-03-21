""" 
- 요청 금액 배정
- 특정한 정수 상한액 배정
"""

N = int(input())
budgets = list(map(int, input().split()))
target = int(input())

budgets.sort()

# 요청 금액 모두 배정 가능한 경우
requirement = sum(budgets)
if requirement <= target:
    print(budgets[-1])
    exit(0)

# 상한액 배정
# requirement - budget
s, e = 0, budgets[-1]
answer = 0
while s <= e:
    m = (s+e) // 2

    x = requirement - sum([ x-m for x in budgets if x > m ])
    if x == target :
        answer = m
        break
    elif x < target :
        answer = m
        s = m+1
    else:
        e = m-1

print(answer)
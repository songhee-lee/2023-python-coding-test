"""Pseudo Code

1. 입력 받고 배열에 저장
2. 5C2 - 중복 숫자의 조합 개수

+. ( 무게 x의 공 개수) x ( 무게 x보다 큰 공의 개수) 의 합
"""

from collections import Counter

# 1. 입력 받기 
N, M = map(int, input().split())
weighs = list(map(int, input().split()))

# 2. 계산
w_count = dict(Counter(weighs))  # 각 무게별 볼링공 개수 카운트
result = N * (N-1) // 2    # nC2

for i in set(weighs):
    x = w_count[i]
    if x > 1:              # xC2 제외하기 
        result -= x * (x-1) // 2

print(result)


####### +. 계산
result_2 = 0
cnt = 0
for i in list(set(weighs))[:-1]:
    print(result_2, i, N - cnt - w_count[i] )
    result_2 += i * (N - cnt - w_count[i])
    cnt += i
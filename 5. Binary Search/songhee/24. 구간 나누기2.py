""" 
- N개의 수로 이루어진 배열
- M개 이하의 구간으로 나눠서 구간 점수의 최댓값을 최소로 하기
    - 구간의 점수 : 최댓값 - 최솟값

*** 풀이
- 구간을 나눌 '기준 값'을 변경해 가면서 나눌 구간 찾기
"""

N, M  = map(int, input().split())
numbers = list(map(int, input().split()))

# 리스트 하나일 때 
if M == 1:
    print(numbers[-1] - numbers[0])
    exit(0)

# 구간 나누기 함수
def divide(target):
    high = low = numbers[0]
    cnt = 1

    for i in range(1, N):
        # ~ i 번째까지 최댓값, 최솟값 구하기
        high = max(high, numbers[i])
        low = min(low, numbers[i])

        # 구간의 점수가 Target 보다 크면 구간 나누기
        if high - low > target :
            cnt += 1
            high = low = numbers[i]
    return cnt  # 나눠진 구간 개수 반환

s, e = 0, max(numbers)
answer = 0
while s <= e:
    m = (s+e) // 2

    if divide(m) <= M : # M개보다 더 많이 나눠졌으면 정답 확인
        e = m-1
        answer = m
    else:
        s = m+1
print(answer)
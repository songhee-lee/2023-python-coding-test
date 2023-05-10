'''
쓰려는 단어가 안끊기면서(다쓰면서)
제일 여백 줄이는 방식으로 쓰기
두 단어 가능하면 한칸 띄워서 작성
'''

import sys

# 표준 입력을 콘솔 입력으로 설정합니다.
input = sys.stdin.readline

# n과 m의 값을 읽어옵니다.
n, m = map(int, input().split())

# 이름들의 길이를 읽어와 'names' 리스트에 저장합니다.
names = [int(input()) for _ in range(n)]

# 'dp' 리스트를 n의 크기로 만들고 무한대로 초기화합니다.
dp = [float('inf')] * n

# 마지막 이름의 길이로 'last_line'을 초기화합니다.
last_line = names[-1]

# 'dp' 리스트의 마지막 원소를 0으로 설정합니다.
dp[-1] = 0

# 끝에서 두 번째 원소부터 첫 번째 원소까지 반복합니다.
for i in range(n-2, -1, -1):
    # 현재 이름의 길이와 1을 더한 후, 마지막 줄의 길이에 더합니다.
    last_line += 1 + names[i]
    # 마지막 줄의 길이가 'm'보다 작거나 같으면 'dp[i]'를 0으로 설정합니다.
    if last_line <= m:
        dp[i] = 0
    else:
        break

# 끝에서부터 시작하여 앞으로 이동하며 'dp[i]' 값을 계산합니다.
for i in range(n-1, -1, -1):
    # 만약 'dp[i]'가 0이면 건너뜁니다.
    if not dp[i]:
        continue
    # 현재 이름의 길이를 'now'에 저장합니다.
    now = names[i]
    # 'dp[i]' 값을 계산합니다.
    dp[i] = min(dp[i], (m-now) ** 2 + dp[i+1])
    # 'now'에 이름들을 더해가며 'dp[i]' 값을 계산합니다.
    for j in range(i + 1, n):
        if now + 1 + names[j] > m:
            break
        now += 1 + names[j]
        dp[i] = min(dp[i], (m - now) ** 2 + dp[j+1])

# 'dp[0]' 값을 출력합니다.
print(dp[0])

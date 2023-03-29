'''
[문제]
- 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임
- 계단 오르는 데는 다음과 같은 규칙이 있다.
    1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
    2. 연속된 세 개의 계단을 모두 밟아서는 안된다. 단, 시작점은 계단에 포함되지 않는다.
    3. 마지막 도착 계단은 반드시 밟아야 한다.
    
- 각 계단에 쓰여 있는 점수가 주어졌을 때, 계단 오르는 데 있는 점수의 최대값을 구하는 프로그램을 작성하시오.

[점화식]
- dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])
    -> i번째 계단에서 얻을 수 있는 점수의 최대값은
        i - 2번째 계단을 밟고 i번째 계단을 밟거나,(두 계단 오르기)
        i - 3번째 계단을 밟고 i - 1, i번째 계단을 밟거나(연속 세개를 밟지 않기 위해)
    -> ✅ i 번째를 밟지 않는 경우는 배제해야 한다. 왜냐하면 마지막 도착 계단은 반드시 밟아야 하기 때문에
'''

n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]

# dp 테이블 (n + 1)개로 초기화 -> 시작점 포함
dp = [0] * (n + 1)
dp[1] = stairs[1]

# 계단이 2개 이상일 때
if n >= 2:
    dp[2] = stairs[1] + stairs[2]

# 점화식
for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

print(dp)
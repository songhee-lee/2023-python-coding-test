""" 
- 계단은 한 번에 하나 또는 두 계단씩 오른다
- 연속된 세 계단을 모두 밟을 수 없다
- 마지막 계단은 반드시 밟아야 한다

- Index 조심!!
"""

N = int(input())
stairs = [ int(input()) for _ in range(N) ]

# dp[x] : x번째 계단까지의 점수 최댓값
dp = [0] * N
dp[0] = stairs[0]

if N > 1:
    dp[1] = stairs[0] + stairs[1]
if N > 2:
    dp[2] = max(dp[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3, N):
    # 1번째로 밟기 VS 2번째로 밟기
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

print(dp[N-1])
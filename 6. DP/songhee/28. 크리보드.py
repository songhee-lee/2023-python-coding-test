""" 
- 4개 버튼을 N번 누를 때 출력할 수 있는 A의 최댓값
- 출력 / 전체 선택 / 복사 / 붙여넣기

"""

N = int(input())

buffer = 0
dp = [ i for i in range(N+1)]

for i in range(6, N+1):
    # 선택 -> 복사 -> 붙여넣기 vs 복붙 반복
    dp[i] = max(dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)

print(dp[N])


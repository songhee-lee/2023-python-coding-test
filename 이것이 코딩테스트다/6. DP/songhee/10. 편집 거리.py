""" 
- A 문자열을 B 문자열로 만들기
- insert / remove / Replace 연산 가능
- 최소 편집 거리 구하기
"""

a = input()
b = input()

n, m = len(a), len(b)

# dp[i][j] : a의 i 번째, b의 j번째 문자에서의 최소 편집 거리
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = i
for j in range(1, m+1):
    dp[0][j] = j

# bottom-up
for i in range(1, n+1):
    for j in range(1, m+1):
        # 문자가 같으면 그대로 사용 (편집 없음)
        if a[i-1] == b[j-1] :
            dp[i][j] = dp[i-1][j-1]
        # 다르면 삽입, 삭제, 교체 중 최소 비용 찾기
        else:
            dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

print(dp[n][m])
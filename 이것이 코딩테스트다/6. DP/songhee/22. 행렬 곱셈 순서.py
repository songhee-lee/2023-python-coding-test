""" 
- NxM 과 MxK 곱하는데 필요한 연산 수는 NxMxK
- 모든 행렬 곱하는데  필요한 곱셈 연산 횟수의 최솟값 구하기
"""

N = int(input())    # 행렬 개수
array = [list(map(int, input().split())) for _ in range(N)]  # 행렬의 크기

# dp[i][j] : i~j 까지 행렬 곱하는데 필요한 연산의 최솟값
dp = [[0]*N for _ in range(N)]

for j in range(N-1):
    dp[j][j+1] = array[j][0] * array[j][1] * array[j+1][1]

for i in range(2, N):       # 행
    for j in range(N-i):    # 열
        dp[j][j+i] = float('inf')
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k]+dp[k+1][j+i]+array[j][0]*array[k][1]*array[j+i][1])

print(dp[0][N-1])

"""
- 1~N 도시 중 M개 도시 지나기
- 최대한 맛있는 기내식 먹기 
"""
N, M, K = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    a, b, c = list(map(int, input().split()))
    graph[a][b] = max(graph[a][b], c)

# dp[i][m] : i 번째 도시까지의 m번 지날 때 최댓값
dp = [[0]*(M+1) for _ in range(N+1)]

for i in range(2, N+1): # 첫번째 도시에서의 이동
    dp[i][2] = graph[1][i]

for i in range(2, N+1):
    for j in range(3, M+1): # 3~M번째 도시까지 이동
        # 이전 도시 ->i 번째 도시
        for k in range(1, i):
            if graph[k][i] and dp[k][j-1]:
                dp[i][j] = max(dp[k][j-1]+graph[k][i], dp[i][j])
print(max(dp[N]))
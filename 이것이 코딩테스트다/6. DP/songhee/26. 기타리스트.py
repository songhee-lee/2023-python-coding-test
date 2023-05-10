""" 
- 0 ~ M 사이로 i번째 곡은 P+v[i] 또는 P-v[i]로 볼륨을 바꾼다.
- 마지막 곡을 연주할 수 있는 볼륨 중 최댓값 구하기
- 마지막 곡을 연주할 수 없으면 -1
"""

# 입력 받기
N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))

# dp[i][m] : i 번째 곡을 볼륨 m 으로 연주 가능 여부
dp = [[-1]*(M+1) for _ in range(N+1)]
dp[0][S] = 1

for i in range(N):
    for now in range(M+1):
        if dp[i][now] == 1:   # i번째 곡 연주 가능한 시간
            up = now + volumes[i]   # 볼륨 UP
            if up <= M : 
                dp[i+1][up] = 1
            down = now - volumes[i] # 볼륨 Down
            if down >= 0:
                dp[i+1][down] = 1

ans = -1
for i in range(M, -1, -1):
    if dp[N][i] == 1:
        ans = i
        break
print(ans)
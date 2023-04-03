'''
[문제]
- 볼륨의 리스트 v가 주어지고, 이 리스트를 순서대로 연주하려고 한다.
- V[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨을 의미한다.
- 현재 볼륨이 P이고 지금 i번째 곡을 연주하기 전이라면, i번 곡은 P + V[i] or P - V[i]로 연주한다.
- 하지만 0보다 작거나 M보다 큰 볼륨으로는 연주할 수 없다.
- 마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구하라

[점화식]
- dp[i][j] = i번째 곡을 볼륨 j로 연주할 수 있는지 없는지

'''

n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

# 시작 볼륨은 s
# 1은 해당 볼륨으로 연주할 수 있음을 의미
dp[0][s] = 1

# 1번째 곡부터 n번째 곡까지
for i in range(1, n + 1):
    for j in range(m + 1):
        
        # i번째 곡을 볼륨 j로 연주할 수 있다면,
        if dp[i - 1][j] != 0:
            up = j + volumes[i - 1] # 볼륨 높이기
            down = j - volumes[i - 1] # 볼륨 낮추기
            
            # 볼륨의 범위를 벗어나지 않는다면,
            if up <= m:
                dp[i][up] = 1
            if down >= 0:
                dp[i][down] = 1
        
# 마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구한다.
ret = -1
for volume in range(m, -1, -1):
    if dp[n][volume] == 1: # 해당 volume으로 연주할 수 있다면
        ret = volume
        break

print(ret)
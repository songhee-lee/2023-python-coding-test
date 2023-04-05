'''

'''
n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [0] * (m + 1)
dp[s] = 1

for i in range(1, n + 1):
    temp = [0] * (m + 1)
    for j in range(m + 1):
        if dp[j] != 0:
            up = j + volumes[i - 1]
            down = j - volumes[i - 1]
            if up <= m:
                temp[up] = 1
            if down >= 0:
                temp[down] = 1
    dp = temp

ret = -1
for volume in range(m, -1, -1):
    if dp[volume] == 1:
        ret = volume
        break

print(ret)

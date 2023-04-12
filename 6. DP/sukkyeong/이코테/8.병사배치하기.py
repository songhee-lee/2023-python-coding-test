'''
병사를 배치할 때 전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치



'''

import sys

# 병사 수 입력받음
n = int(sys.stdin.readline())

soldiers = list(map(int, sys.stdin.readline().split()))
dp = [1]*n

for i in range(n):
    for j in range(i):
        # 내림차순이면
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))

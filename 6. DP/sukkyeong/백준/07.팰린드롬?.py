'''
문자열 S가 주어집니다.
S를 입력받을 때, S[i] ~ S[j]가 팰린드롬인지 판별하여 2차원 배열 dp[i][j]에 저장합니다.
구간 [start, end]가 주어졌을 때, dp[start][end]를 출력합니다.

S[i] == S[j]인 경우
dp[i][j] = dp[i+1][j-1] (i < j)
S[i] != S[j]인 경우
dp[i][j] = False

'''

import sys

# 입력 받기
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

# dp[i][j]는 arr[i] ~ arr[j]가 팰린드롬인지 여부를 저장합니다.
dp = [[0] * N for _ in range(N)]

# 1개짜리 문자열은 모두 팰린드롬입니다.
for i in range(N):
    dp[i][i] = 1

# 2개짜리 문자열도 팰린드롬인지 체크합니다.
for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

# 3개 이상의 문자열에 대해 팰린드롬 여부를 체크합니다.
for k in range(2, N):
    for i in range(N-k):
        j = i + k
        if arr[i] == arr[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

# M개의 질문에 대해 답을 출력합니다.
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(dp[start-1][end-1])

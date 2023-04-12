"""
- 자연수 N 에 대해 질문 Mqjs
- 두 정수 S ~ E 번째 까지 수가 팰린드롬을 이루는지 물어봄
- 대답 구하기 

sys 안하면 시간초과
"""
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())

# dp[s][e] : s~e번째까지 수가 팰린드롬인지 확인
dp = [ [0]*N for _ in range(N)]
for i in range(N):      # 길이가 1 - 자기 자신
    dp[i][i] = 1
for i in range(N-1):    # 길이가 2
    if numbers[i] == numbers[i+1]:
        dp[i][i+1] =1
    
for l in range(2, N):   # len >= 3
    for s in range(N-l):
        e = s + l
        if numbers[s] == numbers[e] and dp[s+1][e-1] == 1:
            dp[s][e] = 1 

for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
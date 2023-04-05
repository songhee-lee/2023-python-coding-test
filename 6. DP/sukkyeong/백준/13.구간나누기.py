'''
각 구간은 한 개 이상의 연속된 수들로 이루어진다.
서로 다른 두 구간끼리 겹쳐있거나 인접해 있어서는 안 된다.
정확히 M개의 구간이 있어야 한다. M개 미만이어서는 안 된다.
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dp1 = [[0]+[-1e9]*M for _ in range(N+1)]
dp2 = [[0]+[-1e9]*M for _ in range(N+1)]

for i in range(1, N+1):
    num = int(input())
    for j in range(1, min((i+1)//2, M)+1):
        dp2[i][j] = max(dp1[i-1][j], dp2[i-1][j])
        dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j-1]) + num

print(max(dp1[N][M], dp2[N][M]))

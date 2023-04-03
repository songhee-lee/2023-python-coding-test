""" 
- 두 파일을 합칠  때 필요한 비용은 두 파일 크기의 합
- 하나의 파일을 완성하는데 필요한 비용의 총 합 계산하기
"""
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    f = [0] + list(map(int, input().split()))

    # files[i] : i까지의 파일 크기의 합
    files = [0] * (K+1)
    for i  in range(1, K+1):
        files[i] = files[i-1] + f[i]
    
    # dp[i][j] : i~j까지 합치는데 필요한 최소 비용
    dp = [ [0]*(K+1) for _ in range(K+1)]
    for i in range(2, K+1):         # 파일의 거리
        for j in range(1, K+2-i):   # 시작점
            # dp[a][m] = dp[m+1][b] + sum(f[a]~f[b])
            dp[j][j+i-1] = min([dp[j][j+k]+dp[j+k+1][j+i-1] for k in range(i-1)]) + ( files[j+i-1] - files[j-1])
    
    print(dp[1][K])

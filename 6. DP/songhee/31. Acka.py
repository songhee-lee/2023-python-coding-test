"""
- S곡을 3명이서 부를 때 앨범을 만들 수 있는 방법의 수 
"""
import math

S, p1, p2, p3 = map(int, input().split())
n = p1+p2+p3
if n < S :   # 불가능한 경우
    print(0)
else:
    # dp[n][a][b][c] : n 번째 곡을 a,b,c가 부를 때 vs 안부를 때 
    dp = [[[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

    def counting(s, a, b, c):
        if s == 0:
            if a == 0 and b == 0 and c == 0:
                return 1    # 모든 곡에 대한 분배 끝
            else:
                return 0    # 잘못 분배함
        
        if a < 0 or b < 0 or c < 0: # 불가능한 경우의 수
            return 0

        if dp[s][a][b][c] != -1 :   # 이미 확인한 경우
            return dp[s][a][b][c]
        
        dp[s][a][b][c] = 0
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    if i + j + k == 0: continue
                    # a, b, c가 부를 때/ 안부를 때 총 7가지 조합 확인
                    dp[s][a][b][c] += counting(s-1, a-i, b-j, c-k)
        dp[s][a][b][c] %= 1000000007
        return dp[s][a][b][c]
    
    print(counting(S, p1, p2, p3))


    
    

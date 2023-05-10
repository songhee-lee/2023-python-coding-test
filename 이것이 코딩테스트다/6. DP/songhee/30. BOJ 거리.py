"""
- 스타트 1번, 링크 N번 집에 있다
- 스타트 -> 링크 이동할 때 필요한 에너지 양의 최솟값
- i번에서 i+1 ~ N까지 점프할 수 있는데, 
    k칸 점프하는데 필요한 에너지 K*k
- B, O, J 순서로 보도블록 밟아야 함
"""
from collections import defaultdict
from collections import deque

N = int(input())
string = input()

idx = {'B':'J', 'O':'B', 'J':'O'}
# dp[i][j] : i~j 까지 가는데 필요한 에너지
dp = [float('inf')]*N
dp[0] = 0

for i in range(1, N):
    prev = idx[string[i]]
    for j in range(i):
        if string[j] == prev:
            dp[i] = min(dp[i], dp[j]+(i-j)**2)

print( dp[N-1] if dp[N-1] != float('inf') else -1)
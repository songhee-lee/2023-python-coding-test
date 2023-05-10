'''
[설명]
- n * m 크기의 금광이 있다. 금광은 1 * 1 크기의 칸으로 나누어져 있고, 각 칸에는 특정한 크기의 금이 들어있다.
- 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다.
- 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있다.
- 이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
- 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하라.

[아이디어]
- 문제에서 주어진 이동 가능한 방향을 적절히 조건문을 사용해서, 얻을 수 있는 금을 차곡차곡 쌓는다.
- 방향 설정은 여러 방법이 있지만, 현재 코드에서는
    - 현재 위치가 오른쪽 위, 오른쪽, 오른쪽 아래라고 가정하고
    - 이전 위치, 즉, 왼쪽 아래, 왼쪽, 왼쪽 위에 있는 금의 크기를 비교한다.

[점화식]
- dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1]) + golds[i][j]
    -> 왼쪽 

'''

import sys

# DP
def dp_helper():
    
    # Bottom-Up (DP 테이블 초기화)
    dp = [[0] * m for _ in range(n)]
    
    # 0 번째 열에서 얻을 수 있는 금의 크기 초기화
    for row in range(n):
        dp[row][0] = golds[row][0]
    
    
    # 1 번째 열부터 시작
    for j in range(1, m):
        # 모든 행에 대해서
        for i in range(n):
            # 왼쪽 위 : (i - 1, j - 1)
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + golds[i][j])
            # 왼쪽 : (i, j - 1)
            if j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + golds[i][j])
            # 왼쪽 아래 : (i + 1, j - 1)
            if i + 1 < n and j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + golds[i][j])
    
    # 최대로 캘 수 있는 금의 크기 찾기
    max_gold = 0
    for i in range(n):
        max_gold = max(max_gold, dp[i][m - 1])
        
    return max_gold

# 테스트 케이스 입력
t = int(input())

# 입력 처리
for _ in range(t):
    n, m = map(int, input().split())
    gold_pos = list(map(int, input().split()))
    
    golds = []
    
    index = 0
    for i in range(n):
        golds.append(gold_pos[index:index + m])
        index += m
    
    # dp 수행
    print(dp_helper())
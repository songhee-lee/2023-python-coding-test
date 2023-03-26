'''
[설명]
- 정수 삼각형의 맨 위층부터 시작해서, 아래에 있는 수 중 하나를 선택해서 아래층으로 내려온다.
- 이때 이제까지 선택된 수의 합의 최댓값을 출력하라
- 단, 이동 가능한 방향은 '대각선 왼쪽 아래' 또는 '대각선 오른쪽 아래'이다.

[아이디어]
- 현재 위치 : (i, j)
    - 대각선 왼쪽 아래 : (i + 1, j)
    - 대각선 오른쪽 아래 : (i + 1, j + 1)
- 위의 규칙을 적용해서, 맨 아래층까지 dp를 수행한다.
- 최종적으로 (n - 1)행에서 합의 최댓값을 찾아서 출력한다.

- ✅ 정수 삼각형의 구조를 살펴보면
    - 행 인덱스가 0이면, 열은 1개
    - 행 인덱스가 1이면, 열은 2개 ...
-> 즉, 열의 개수는 (행 인덱스 + 1)개이다. 
-> 이를 토대로 for문을 수행해야 한다.

[점화식]
- 

'''

import sys

# sol - 1
# dp
def dp_helper():
    dp = [[0] * i for i in range(1, n + 1)] # 정수 삼각형의 구조에 맞게 dp 테이블 초기화    
    dp[0][0] = triangle[0][0]
    
    # 맨 위층에서 시작
    for row in range(n):
        for col in range(row + 1):
            if row + 1 < n:
                # 왼쪽 대각선 아래
                dp[row + 1][col] = max(dp[row + 1][col], dp[row][col] + triangle[row + 1][col])
                
                # 오른쪽 대각선 아래
                if col < row + 1:
                    dp[row + 1][col + 1] = max(dp[row + 1][col + 1], dp[row][col] + triangle[row + 1][col + 1])
    
    return max(dp[n - 1])         

# sol - 2
def dp_helper2():
    dp = [[0] * i for i in range(1, n + 1)] # 정수 삼각형의 구조에 맞게 dp 테이블 초기화    
    dp[0][0] = triangle[0][0]
    
    for row in range(1, n):
        col_start, col_end = 0, row
        
        # 양 끝 점은 위층의 숫자가 그대로 내려온다.
        dp[row][col_start] = dp[row - 1][col_start] + triangle[row][col_start]
        dp[row][col_end] = dp[row - 1][col_end - 1] + triangle[row][col_end]
        
        # 양 끝 점 사이의 원소들 DP
        for col in range(col_start + 1, col_end):
            dp[row][col] = max(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]
    
    return max(dp[n - 1])

n = int(input())

triangle = []

for _ in range(n):
    input_data = list(map(int, input().split()))
    triangle.append(input_data)

# dp 수행
print(dp_helper2())


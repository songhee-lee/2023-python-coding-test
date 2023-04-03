'''
[문제]
- 크기가 N * M 인 행렬 A와 M * K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N * M * K이다.
- 행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라진다.
- 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하라

[점화식]
- dp[i][j] = 행렬 i와 행렬 j를 곱할 때 필요한 곱셈 연산의 수의 최솟값
    -> 경유지를 설정하여 dp[i][j]를 구한다.
    => dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])

- ex) A B C D => ABCD
        -> A(BCD) -> A(B(CD)) or A((BC)D)
        -> (AB)(CD) 
        -> (ABC)(D) -> (A(BC))(D) or ((AB)C)(D
        
✅ 다시 풀기, 파일 합치기와 유사한 문제, Python3는 시간 초과
'''

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] = 행렬 i와 행렬 j를 곱할 때 필요한 곱셈 연산의 수의 최솟값
dp = [[0] * n for _ in range(n)]

for gap in range(1, n): # 간격(거리)
    for _from in range(n): # 시작 행렬
        _to = _from + gap # 끝 행렬
        
        if _to >= n: # 범위를 벗어난다면
            break
            
        dp[_from][_to] = float('inf') # 최솟값을 구해야 하므로
        
        # 경유지를 설정한다.
        for via in range(_from, _to):
            dp[_from][_to] = min(dp[_from][_to], dp[_from][via] + dp[via + 1][_to] + matrix[_from][0] * matrix[via][1] * matrix[_to][1])

# 점화식을 채워넣으면, 마지막 값이 모든 행렬을 곱했을 때 
# 필요한 곱셈 연산 수의 최솟값이 된다.
print(dp[0][-1])
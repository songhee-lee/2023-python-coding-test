def solution(matrix_sizes):
    n = len(matrix_sizes)
    M = matrix_sizes
    
    # dp[i][j] : i ~ j번째까지의 행렬 곱셈을 할 때 최소의 연산 수
    dp = [[0]*n for _ in range(n)]
    
    # i < j인 부분만 값을 채우는데,
    # d = j-i 의 값이 1, 2, ..., n-1 인 쌍의 순서대로 값 채우기.
    for d in range(1, n) : 
        for i in range(n) :
            j = i + d
            if j >= n : break   # 범위를 벗어나는 경우
            
            if d == 1 :         # 첫 번째 행렬 곱셈이 된 경우
                dp[i][j] = M[i][0] * M[i][1] * M[j][1]
            else :              
                candidates = [] # 모든 경우의 수를 구한 뒤 최솟값 찾기
                for k in range(d) :
                    # i ~ i+k 행렬까지 최소의 곱셈연산 수
                    # i+k+1 ~ j 행렬까지 최소의 곱셈연산 수
                    # (i~i+k) * (i+k+1~j) 두 행렬의 곱셈 연산 수
                    candidates.append(dp[i][i+k] + dp[i+k+1][j] + M[i][0] * M[i+k][1] * M[j][1]) 
                dp[i][j] = min(candidates)
                
    return dp[0][n-1]
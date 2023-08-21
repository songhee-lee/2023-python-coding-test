def solution(s):
    n = len(s)
    # dp[i][j] : i~j 문자열 중 가장 긴 팰린드롬의 길이
    dp = [[False]*n for _ in range(n)]
    # dp 초기화
    for i in range(n-1) :
        dp[i][i] = True         # 길이가 1인 문자열
        if s[i] == s[i+1] :     # 길이가 2인 문자열
            dp[i][i+1] = True
    dp[n-1][n-1] = True
    
    for d in range(2, n):       # 길이가 3 ~ n-1인 문자열
        for start in range(n-d):
            end = start + d
            if end > n : break
            
            if s[start] == s[end] and dp[start+1][end-1] :
                dp[start][end] = True
    
    # 가장 긴 문자열 길이 구하기
    answer = 1
    for start in range(n) :
        for end in range(start+1, n) :
            if dp[start][end] :
                answer = max(answer, end-start+1)
    return answer
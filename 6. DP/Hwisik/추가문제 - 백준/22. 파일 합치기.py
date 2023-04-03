'''
[문제]
- 소설의 각 장을 합쳐서 파일 하나로 만들려고 한다.
- 인접한 페이지끼리만 합칠 수 있다.
- 파일들을 하나의 파일로 합칠 때 필요한 최소비용을 계산하라.

[점화식]
- dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sum(i ~ j))
    -> k번 페이지를 거친다면, (i ~ k) 구간과 (k + 1 ~ j) 구간으로 나누어서 합친다.
        -> (i ~ k) 구간은 dp[i][k]로, (k + 1 ~ j) 구간은 dp[k + 1][j]로 계산할 수 있다.
            -> 그 후, 구간의 합을 추가로 더해야 한다.
- ex. C1 ~ C3 합치는 비용은 dp의 값 + (C1 + C2 + C3)이다.

✅ 답 참고함, 다시 풀기, Python3는 '시간 초과'
'''

t = int(input())

for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    
    # 구간의 합을 저장할 리스트
    continuous_sum = [0] * (k + 1)
    for i in range(k):
        continuous_sum[i] = continuous_sum[i - 1] + files[i]
    
    # dp[i][j] = i ~ j 구간을 합치는데 필요한 최소 비용
    dp = [[0] * k for _ in range(k)]
    
    # 시작 페이지와 끝 페이지의 간격(거리)
    for gap in range(1, k):
        for _from in range(k): # 시작 페이지
            _to = _from + gap # 끝 페이지
            
            if _to >= k: # 범위를 벗어나면 break
                break
            
            # 최소 비용을 찾기 위해 초기화
            dp[_from][_to] = float('inf')
            
            # 중간 페이지를 기준으로 나누어서 비용을 계산
            for via in range(_from, _to):
                dp[_from][_to] = min(dp[_from][_to], dp[_from][via] + dp[via + 1][_to] + continuous_sum[_to] - continuous_sum[_from - 1])
                
    # for i in range(k - 2):
    #     for j in range(i + 1, k - 1):
    #         for l in range(j + 1, k):
    #             dp[i][l] = min(dp[i][l], files[i] + dp[j][l], dp[i][j] + files[l])
    
    print(dp[0][-1])
'''
[문제]
- N개의 수로 이루어진 1차원 배열이 있다.
- 이 배열에서 M(1 <= M <= N/2)개의 구간을 선택해서, 구간에 속한 수들의 총 합이 최대가 되도록 하려고 한다.
    1. 각 구간은 한 개 이상의 연속된 수들로 이루어진다.
    2. 서로 다른 두 구간끼리 겹쳐있거나 인접해 있어서는 안된다.
    3. 정확히 M개의 구간이 있어야 한다. M개 미만이어서는 안된다.
- 구간에 속한 수들의 총 합이 최대가 되는 값을 구해보자.

🌠 모든 수가 구간에 들어갈 필요는 없다.

[점화식]
- dp[i][j]
    - exclude_dp[i][j] : i - 1번째 수를 포함하지 않는 경우
    - include_dp[i][j] : i - 1번째 수를 포함하는 경우
    
✅ 답 참고함, 다시 풀기
'''
from pprint import pprint

n, m = map(int, input().split())
_list = [int(input()) for _ in range(n)]

include_dp = [[0] + [-1e9] * m for _ in range(n + 1)]
exclude_dp = [[0] + [-1e9] * m for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, min(m, (i + 1) // 2) + 1):
        exclude_dp[i][j] = max(include_dp[i - 1][j], exclude_dp[i - 1][j])
        include_dp[i][j] = max(include_dp[i - 1][j], exclude_dp[i - 1][j - 1]) + _list[i - 1]
    
print(max(include_dp[n][m], exclude_dp[n][m]))

########################################

# 시간 초과
# def solution_1():
#     # 구간의 합을 저장할 리스트
#     dp = [[0] * n for _ in range(n)]

#     # 자기 자신도 구간에 포함
#     for i in range(n):
#         dp[i][i] = _list[i]

#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             dp[i][j] = dp[i][j - 1] + _list[j]
            
#     ret = 0

#     def helper(cnt, idx, _sum):
#         global ret
#         if idx >= n:
#             return
        
#         if cnt == m:
#             ret = max(ret, _sum)
#             return
        
#         for i in range(idx + 2, n):
#             for j in range(i, n):
#                 helper(cnt + 1, j, _sum + dp[i][j])

#     helper(0, -2, 0)

#     print(ret)    


# solution_1()
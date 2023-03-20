'''
- 산성 용액 : [1 , 1,000,000,000]
- 알칼리성 용액 : [-1,000,000,000 , -1]
- 혼합 방법 : 산성 + 산성 / 알칼리성 + 알칼리성 / 산성 + 알칼리성
- 두 용액을 더하면서...
    - 더한값이 0에 더 가깝다면, 갱신한다.
    - 더한값이 0보다 크다면, r -= 1
    - 더한값이 0보다 작다면, l += 1

-> ✅다시풀기
'''

import sys

# 이진 탐색
def binary_search():
    l, r = 0, n - 1
    value = 2e9 # 비교 변수 => ('산성 + 산성'도 가능하므로, 최대값은 2e9)
    ans_l, ans_r = 0, 0 # 특성값이 0에 가장 가까운 두 용액의 인덱스
    
    while l < r:
        cur_sum = solution[l] + solution[r] # 두 용액을 더한 특성값
        
        # 0에 더 가깝다면
        if value > abs(cur_sum):
            value = abs(cur_sum) # 갱신
            ans_l, ans_r = l, r # 갱신
            if value == 0: # 특성값이 0이라면
                break # 더 이상 비교는 필요 X
            
        if cur_sum < 0:
            l += 1
        else:
            r -= 1
            
    return (ans_l, ans_r) # 특성값이 0에 가장 가까운 용액 2개 반환
        
        
n = int(sys.stdin.readline())
solution = list(map(int, sys.stdin.readline().split()))

# 이진 탐색 수행
ret_l, ret_r = binary_search()

# 출력
print(solution[ret_l], solution[ret_r])
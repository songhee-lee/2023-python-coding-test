'''
- 이진탐색 수행 전, 예산 리스트를 정렬
- l, r을 1과 요청 예산의 총 합으로 설정
- mid를 구하고, 예산을 배정한다.
- 배정된 예산이 m보다 작거나 같다면, 상한가액을 높일 수 있으므로, l = mid + 1
- 배정된 예산이 m보다 크다면, 상한가액을 낮춰야하므로, r = mid - 1
'''

import sys

# 이진 탐색
def binary_search():
    l, r = 1, budget_sum
    
    answer = 0
    while l <= r:
        mid = l + (r - l) // 2
        
        # 예산 배정
        can_afford_budget = 0
        for budget in budgets:
            
            # 조건 1.
            if budget < mid:
                can_afford_budget += budget
            # 조건 2.
            else:
                can_afford_budget += mid
        
        # 상한가액이 낮게 설정된 경우, 오른쪽 부분탐색
        if can_afford_budget <= m:
            l = mid + 1
            answer = mid
            
        # 상한가액이 너무 높게 설정된 경우, 왼쪽 부분탐색
        else:
            r = mid - 1
            
    # 상한가액 최댓값 반환
    return answer

n = int(sys.stdin.readline())
budgets = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())

budget_sum = sum(budgets) # 요청 예산의 총 합

# 요청 예산의 총 합을 지급해줄 수 있는 경우
# 배정된 예산들 중 최댓값 출력
if budget_sum <= m:
    print(budgets[-1])
    
# 총 예산이 부족한 경우
# 이진 탐색 수행
else:
    ret = binary_search()
    print(ret)
'''
- 
'''
from collections import deque

# sol 1
def solution(queue1, queue2):
    
    # 시간 줄이기 & pop, insert 쉽게 하기 -> deque
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    
    # 각 deque의 합
    dq1_sum = sum(dq1)
    dq2_sum = sum(dq2)
    
    # 합이 같다면 교환이 필요 없다.
    if dq1_sum == dq2_sum:
        return 0
    
    # 두 큐의 합
    total_sum = dq1_sum + dq2_sum
    
    # 두 큐의 총합이 홀수라면, 두 큐의 합을 같게 할 수 없다.
    if total_sum % 2 != 0:
        return -1
    
    max_change_count = len(dq1) * 3 # 이거 왜 3번 해야됨?
    count = 0
    
    while dq1_sum != dq2_sum:
        # dq1의 합이 더 크면
        if dq1_sum > dq2_sum:
            popped_val = dq1.popleft() # 첫 번째 원소 추출
            
            # 합 갱신
            dq1_sum -= popped_val 
            dq2_sum += popped_val
            
            # dq2의 마지막에 추출한 원소 추가
            dq2.append(popped_val)        
        
        # dq2의 합이 더 크면
        elif dq2_sum > dq1_sum:
            popped_val = dq2.popleft() # 첫 번째 원소 추출
            
            # 합 갱신
            dq2_sum -= popped_val
            dq1_sum += popped_val
            
            # dq1의 마지막에 추출한 원소 추가
            dq1.append(popped_val)
            
        # 두 큐의 합이 같다면
        else:
            return count
        count += 1
        
        # 어떤 방법을 쓰더라도
        # 각 큐의 원소 합을 같게 만들 수 없는 경우
        if count >= max_change_count:
            return -1
           
    return count

# sol 2

'''
- while문 보다 for문이 빠르다. -> while문의 조건절 연산이 없어서...
'''
def solution(queue1, queue2):
    answer, sum1, sum2, max_change_count = 0, sum(queue1), sum(queue2), len(queue1) * 3
    dq1, dq2 = deque(queue1), deque(queue2)
    
    for _ in range(max_change_count):
        if sum1 > sum2:
            popped_val = dq1.popleft()
            sum1 -= popped_val
            sum2 += popped_val
            dq2.append(popped_val)
        elif sum1 < sum2:
            popped_val = dq2.popleft()
            sum2 -= popped_val
            sum1 += popped_val
            dq1.append(popped_val)
        else:
            return answer
        
        answer += 1
    
    # for-else
    # for문이 중간에 return이 안될 경우
    # 즉, 최대 비교 횟수를 넘어가는 경우
    else:
        return -1
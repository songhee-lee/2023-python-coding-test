""" 
- 각 큐의 원소 합 같도록 만들기 위한 최소 횟수 (pop+insert 가 1회)

"""
from collections import deque

def solution(queue1, queue2):
    
    # 시작, 끝 포인터로 표시
    q = queue1 + queue2
    s, e = 0, len(queue1)-1
    now, target = sum(queue1), sum(q) // 2
    n = len(q)
    answer = 0
    
    # 원소 합을 같게 만들 수 없는 경우
    # 1) 두 큐의 원소 합이 홀수
    if sum(q) % 2 != 0 :   
        return -1
    
    # 2) 큰 숫자가 존재
    if sum(q) <= max(q):
        return -1
    
    while now != target:       
        
        # q2 -> q1
        if now < target :
            e += 1
            if e == n : # 중간 탈출 조건
                return -1
            now += q[e]

        # q1 -> q2
        else:
            now -= q[s]    
            s += 1

        answer += 1
    return answer

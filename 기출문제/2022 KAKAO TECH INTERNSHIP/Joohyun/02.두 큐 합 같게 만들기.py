"""
두 개의 큐
1. 하나의 큐를 골라 원소를 추출 : pop
2. 추출된 원소를 다른 큐에 삽입 : insert
>> sum(큐1)==sum(큐2) 도록 하는 작업의 최소 횟수

작업 = pop + insert

예외 처리 : 각 큐의 원소 합을 같게 만들 수 없으면 -> return -1
"""
"""
< FLOW >
두 큐의 합이 같아지도록 반복
1. 두 큐의 합을 비교
2. 합이 큰 큐에서 pop , 합이 작은 큐에 insert
3. 작업 횟수 증가

반복 탈출 조건 :
1. 두 큐의 합이 같아진 경우
2. 너무 많이 반복했을 경우 : 작업 횟수 제한 (큐 길이의 n 배)
"""
from collections import deque

def solution(queue1, queue2):
    queue1,queue2 = deque(queue1),deque(queue2)
    work=0                  # 작업 횟수
    limit = len(queue1) * 3 # 작업 횟수 제한
    sum_1,sum_2 = sum(queue1), sum(queue2)

    # 큐들의 합이 2의 배수가 아니면 두 큐의 합을 같게 할 수 없다
    if (sum_1+sum_2)%2 : return -1

    # 두 큐의 합이 같아질 때까지 반복
    while True :
        # 두 큐의 합이 같아지면 작업 횟수 반환
        if sum_1 == sum_2 : return work

        # 작업을 지나치게 많이 수행했을 경우 >> 두 큐의 합을 같게 만들 수 없는 경우로 간주
        if work > limit : return -1

        # 두 큐의 합이 다를 경우
        if sum_1>sum_2:                         # 큐1 > 큐2 -> 큐1에서 pop + 큐2에 insert
            q1=queue1.popleft()                 # 큐1에서 pop
            queue2.append(q1)                   # 큐2에 insert
            sum_1,sum_2 = sum_1-q1, sum_2+q1    # 합계 update

        else :                                  # 큐1 < 큐2 -> 큐2에서 pop + 큐1에 insert
            q2=queue2.popleft()                 # 큐2에서 pop
            queue1.append(q2)                   # 큐1에 insert
            sum_1,sum_2 = sum_1+q2, sum_2-q2    # 합계 update

        work+=1                                 # 작업 횟수 1 증가


print(solution([3, 2, 7, 2],[4, 6, 5, 1]))  # 2
# 14, 16 >> [32724] [651] >> 1
# 18, 12 >> [2724] [6513] >> 2
# 15, 15 >> return 2
print(solution([1, 2, 1, 2],[1, 10, 1, 2])) # 7
print(solution([1, 1],[1, 5]))              # -1
print(solution([1,4],[4,8]))                # -1
print(solution([1,2,4],[3,2,4]))            # -1
print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 10],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]))    # -1
print(solution([1, 1, 1, 1, 1],[1, 1, 1, 9, 1]))    # 12
#  7, 9 >> [1243] [24] >> 1
# 10, 6 >> [245] [241] >> 2
# 11,

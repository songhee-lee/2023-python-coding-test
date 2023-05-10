"""Pseudo Code

1-1. (예외 처리) 음식 개수가 K초 보다 작다면 K+1 번이 다음 순서가 됨
1-2. (예외 처리) 섭취해야 할 음식이 없으면 -1 반환
2. 음식의 times가 작은 순서대로 정렬하고,
3. 정렬된 순서대로 ( x초 * 음식 개수 ) 만큼 초 세기.

"""

import heapq

def solution(food_times, k):

    # 1-1. 음식 개수가 K초 보다 작다면 K+1 번이 다음 순서가 됨
    if k <= len(food_times) * min(food_times): 
        return k % len(food_times) + 1

    # 1-2. 섭취해야 할 음식이 없으면 -1 반환
    if k >= sum(food_times):
        return -1

    # 2. 음식 times 작은 순서대로 정렬
    heap = []
    for i, x in enumerate(food_times): 
        heapq.heappush(heap, (x, i+1))

    # 3. 순서대로 K - ( x초 * 음식 개수 )
    prev = 0            # 지나간 초 (누적)
    n = len(food_times) # 남은 음식 개수
    while k >= (heap[0][0] - prev) * n:   # 다음 음식을 다 먹을 수 있는지 확인
        now = heapq.heappop(heap)[0]  # 현재 음식을 다 먹는데 걸리는 시간
        k -= now * n   # 음식 한 개를 다 먹을 때까지 회전판 돌아감
        n -= 1         # 음식 개수 차감
        prev += now    # 지나간 초 누적
    
    result = sorted(heap, key=lambda x: x[1])   # 음식 번호 순으로 다시 정렬
    return result[ k % n ][1]    # 남은 초 동안 먹고난 후 돌아오는 음식 번호
    

print(solution([4,2,3,6,7,1,5,8], 16))



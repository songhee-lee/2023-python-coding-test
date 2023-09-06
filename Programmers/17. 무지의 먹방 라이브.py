'''
1~N의 번호
1번부터 음식 먹기 시작
마지막 번호 먹으면 다시 1번
음식 하나를 1초 먹고 다음 번호 먹음

K 초 후에 방송 중단. 다시 방송 이어갈때 몇 번부터 먹어?

food_times : 각 음식마다 모두 먹는 시간
k : 네트워크 장애 발생 시간 (방송 중단 시간)
'''
import heapq


def solution(food_times, k):
    answer = -1
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))

    food_num = len(food_times)  # 남은 음식 개수
    previous = 0  # 이전에 제거한 음식의 food_time

    while h:
        # 먹는데 걸리는 시간: (남은 양) * (남은 음식 개수)
        t = (h[0][0] - previous) * food_num
        # 시간이 남을 경우 현재 음식 빼기
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(h)
            food_num -= 1
        # 시간이 부족할 경우(음식을 다 못먹을 경우) 남은 음식 중에 먹어야 할 음식 찾기
        else:
            idx = k % food_num
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break

    return answer

'''
def solution(food_times, k):
    cur = 0
    food_kind = len(food_times)
    for i in range(k):
        while food_times[cur] == 0:
            cur += 1
            if cur >= food_kind:
                cur = 0
        
        food_times[cur] -= 1
    
        
        cur += 1
        if cur >= food_kind:
            cur = 0
    return cur + 1
'''

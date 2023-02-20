import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    # 시간이 적은 음식부터 빼야 하므로 우선순위 큐 사용
    hq = []
    n = len(food_times)
    
    for i in range(1, n + 1):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(hq, (food_times[i - 1], i))
                       
    sum_value = 0 # 먹기 위해 사용한 시간
    prev = 0 # 이전에 다 먹은 음식 시간(이전에 다 먹은 음식에 걸린 시간)
                       
    # (현재 음식 시간 - 이전에 다 먹은 음식에 걸린 시간) * 현재 음식 개수 <= k - 먹기 위해 사용한 시간 -> 비교
    while ((hq[0][0] - prev) * n) <= k - sum_value:
        now = heapq.heappop(hq)[0]
        sum_value += (now - prev) * n
        n -= 1 # 다 먹은 음식은 제외한다.
        prev = now # 이전 음식 시간 재설정
        
    # 남은 음식 중에서 몇 번째 음식인지 확인한다.
    ret = sorted(hq, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬 -> 무지는 1번 음식부터 먹기 시작하므로
    return ret[(k - sum_value) % n][1]
"""
- 트럭에 재활용 상자 cap 만큼 실을 수 있고
- 트럭은 각 집에 배달하면서 빈 재활용 택배 상자들 수거 후 물류 창고에 내림
- 각 집마다 배달할 재활용 택배 상자의 개수와 수거할 빈 재활용 택배 상자의 개수를 알고 있을 때, 트럭 하나로 모든 배달과 수거를 마치고 물류창고까지 돌아올 수 있는 최소 이동 거리 구하기

- 마지막 집을 먼저 가기 (어차피 가야함!)
"""
def starting_point(array) :
    for i in range(len(array)-1, -1, -1) :
        if array[i] != 0 :
            return i
        else :
            array.pop()

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    if sum(deliveries) + sum(pickups) == 0 :
        return 0
    
    while deliveries or pickups :
        start_d, start_p = 0, 0
        cnt_d, cnt_p = 0, 0
        
        # 배달
        if deliveries :
            start_d = starting_point(deliveries)
            while True :
                if not deliveries: break
                if cnt_d + deliveries[-1] <= cap :
                    cnt_d += deliveries[-1]
                    deliveries.pop()
                else:
                    deliveries[-1] -= (cap - cnt_d)
                    cnt_d = cap
                    break
        
        # 수거
        if pickups :
            start_p = starting_point(pickups)
            while True :
                if not pickups: break
                if cnt_p + pickups[-1] <= cap :
                    cnt_p += pickups[-1]
                    pickups.pop()
                else:
                    pickups[-1] -= (cap - cnt_p)
                    cnt_p = cap
                    break

        # 거리 더하기
        answer += max(start_d, start_p) + 1
        
    return answer * 2
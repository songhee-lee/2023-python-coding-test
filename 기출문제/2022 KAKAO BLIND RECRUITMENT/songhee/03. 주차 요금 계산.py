"""
- 출차 내역 없으면 23:59 출차
- 초과 시간이 단위 시간으로 나누어 떨어지지 않으면 올림

** 나갔다가 다시 들어올 수 있음..
"""
from collections import defaultdict

def calc_time(time_in, time_out):
    "총 주차한 시간을 '분' 단위로 리턴"
    in_h, in_m = map(int, time_in.split(':'))
    out_h, out_m = map(int, time_out.split(':'))
    
    a_h, a_m = 0, 0
    a_m = (out_m - in_m) if out_m > in_m else (out_m+60)-in_m
    a_h = (out_h - in_h) if out_m > in_m else (out_h-1)-in_h
    
    return a_h*60+a_m
    
def solution(fees, records):    
    
    # 자동차별 입/출차 기록
    car_list = defaultdict(list)   # car_list[자동차번호] = (입차시간, 출차시간)
    for record in records:
        time, car_num, state = record.split()
        
        if state == "IN":
            car_list[car_num].append(["", ""])
            car_list[car_num][-1][0] = time
        else:
            car_list[car_num][-1][1] = time
    
    answer = []
    for car_num in sorted(car_list):    # 차량번호가 작은 것부터 확인
        # 출차 시간없으면 23:59로 업데이트
        if car_list[car_num][-1][1] == '':
            car_list[car_num][-1][1] = '23:59'
        
        # 총 주차 시간 계산
        total_time = 0
        for time_in, time_out in car_list[car_num]:
            total_time += calc_time(time_in, time_out)
        
        # 주차 시간이 기본 시간보다 적으면
        if total_time <= fees[0] :  
            cost = fees[1]  # 기본요금
        # 그 이상 주차했으면
        else:   
            if (total_time-fees[0]) % fees[2] == 0:
                cost = fees[1] + (total_time-fees[0])//fees[2] * fees[3]
            else:
                cost = fees[1] + ((total_time-fees[0])//fees[2]+1) * fees[3]
        answer.append(cost)
        
    return answer
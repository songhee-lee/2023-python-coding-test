'''
- 입차한 내역이 없는데 출차하는 경우는 주어지지 않는다 
    -> 입/출차를 따로 처리할 필요 없다.(입차를 하면 무조건 출차 내역이 따라온다.)
    -> 입차-출차-입차-출차 ... 무조건 이런 형태로 입력이 주어진다.
    -> 2개씩 카운트하면서 누적 시간을 계산하면 된다.
    
- 입차했는데 출차하지 않은 경우만 처리해주면 된다. -> 이때는 23:59에 출차한 것으로 간주한다.
'''
from collections import defaultdict
import math

# 출차내역이 없을 때, 23:59에 출차임을 표시하기 위한 변수(단위: 분으로 변환)
_max_out = 1439

# HH:MM을 '분'으로 변환
def time_formatting(time):
    hour, minute = time.split(":")
    
    return int(hour) * 60 + int(minute)

def solution(fees, records):
    answer = []
    
    # 차량 번호별 입/출차 기록
    in_and_out = defaultdict(list) # key: 차량 번호, value: [입차-출차 기록]
    
    for record in records:
        info = record.split(" ")
        
        # 시각, 차량번호
        time, car_num = info[0], info[1]
        
        formatted_time = time_formatting(time) # 시간 변환
        in_and_out[car_num].append(formatted_time) # 추가
    
    # 차량 번호가 작은 자동차부터 return 해야하므로, 정렬을 먼저 한다.
    for key in sorted(in_and_out.keys()):
        if len(in_and_out[key]) % 2 != 0: # 입차했는데 마지막 출차가 없는 경우
            in_and_out[key].append(_max_out) # 계산 편하게 하기 위해 23:59 추가
            
        _sum = 0 # 누적 주차 시간
        
        # 누적 주차 시간 계산
        for i in range(1, len(in_and_out[key]), 2):
            # 입차를 한 뒤에 무조건 출차이므로, i - 1번째가 입차, i번쨰가 출차가 된다. (예외 없음)
            _in, _out = in_and_out[key][i - 1], in_and_out[key][i]
            _sum += (_out - _in)
        
        # 기본 시간안에 해결했으면
        if _sum <= fees[0]:
            answer.append(fees[1]) # 기본 요금 추가
            
        # 기본 시간 오버했으면
        else:
            # 기본 요금 + ((누적 주차 시간 - 기본 시간) / 단위 시간) * 단위 요금
            total = fees[1] + math.ceil((_sum - fees[0]) / fees[2]) * fees[3]
            answer.append(total) # 추가
                
    return answer
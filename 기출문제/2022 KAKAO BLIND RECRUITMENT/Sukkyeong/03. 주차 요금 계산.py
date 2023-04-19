'''
주차장 요금표
입출차 기록
자동차별 주차 요금을 계산
분으로 통일(시간일 경우  n*60)
10으로 나눠서 나머지있으면 그냥 한번에 더함
이 모든 것에 600원을 곱해서 최종 가격을 도출
기본요금 +


'''
import math
def solution(fees, records):
    check = {}
    for record in records:
        time, number, status = record.split()
        time = time.split(':')
        time = int(time[0])*60 + int(time[1])
        if number not in check:
            check[number] = (0, time, status)
        if status == 'IN':
            check[number] = (check[number][0], time, status)
        elif status == 'OUT':
            total_time, in_time, _ = check[number]
            total_time += time - in_time
            check[number] = (total_time, time, status)
    result = {}
    for number in check.keys():
        total_time, time, status = check[number]
        if status == 'IN':
            total_time += 1439 - time
        fee = fees[1]
        if total_time <= fees[0]:
            result[number] = fee
        else:
            fee = fee + math.ceil((total_time - fees[0]) / fees[2]) * fees[-1]
            result[number] = fee

    return list(map(lambda x : x[1], sorted(result.items())))
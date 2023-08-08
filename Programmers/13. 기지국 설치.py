"""
전파 범위가 w인 5g 기지국을 최소로 설치하면서 모든 아파트에 전파를 전달하기
1 <= 아파트의 개수 <= 200,000,000
1 <= 스테이션 크기 <= 10,000
"""
import math

def solution(n, stations, w):
    answer = 0
    now = 1

    if stations[0] < w :
        now = stations[0] + w + 1
        
    for station in stations :
        if station - w > now :
            answer += math.ceil((station-w-now) / (2*w + 1))
        now = station + w + 1
          
    if now <= n :
        answer += math.ceil((n+1-now) / (2*w + 1))
    
    return answer

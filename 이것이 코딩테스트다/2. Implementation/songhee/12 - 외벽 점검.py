"""Psuedo Code
https://school.programmers.co.kr/learn/courses/30/lessons/60062

- 외벽 둘레 N, 취약 지점 weak, 친구의 이동 가능 거리 dist
- 점검 시간 1시간 제한
- 취약 점검을 위해 보내야 하는 친구 수의 최솟값

* 많이 이동 가능한 친구부터 점검 가능한 경우의 수 파악하기

"""

from itertools import permutations

def check(order, weak, dist):
    count = 0
    
    for friend in dist :     # 많이 이동 가능한 친구부터
        for i in range(len(weak)-1) :
            d = abs(order[i+1] - order[i])
            d = min(d, abs(12-d))
            if d <= friend:
                count += 1
                friend -= d
                weak
            else :
                break
    

def solution(n, weak, dist):

    # 취약점 표시하기 (반시계방향 추가)   !!! point
    length = len(weak)
    for i in range(length) :
        weak.append(weak[i]+n)
    
    # 정답 초기화
    answer = len(dist) + 1

    # 각 취약점 시작 포인트 별로 
    for start in range(length):
        # 친구들 투입 순서별로
        for friends in list(permutations(dist, len(dist))): 
            count = 1   # 투입 친구 숫자
            
            # 첫번째 친구의 점검 가능한 마지막 위치
            loc = weak[start] + friends[count-1]

            # 모든 취약지점 점검 가능한지 확인
            for i in range(start, start+length):
                if loc < weak[i] :  # 점검 못하면 다음 친구 투입
                    count += 1
                    if count > len(dist) :  # 친구를 더 투입하지 못하면 종료
                        break
                    loc = weak[i] + friends[count-1]
            
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    
    return answer
        

                    
            
            

        
    return answer


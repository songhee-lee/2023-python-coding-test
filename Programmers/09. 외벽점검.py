'''
레스토랑의 구조 : 완전히 동그란 모양
외벽의 총 둘레 : n미터
외벽의 몇몇 지점 : 취약한 지점 존재
점검 시간을 1시간으로 제한
친구들이 1시간 동안 이동할 수 있는 거리는 제각각
최소한의 친구 - 취약 지점 점검 / 나머지 친구 - 내부 공사

취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리
친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동합니다.

n: 외벽의 길이 (1~200)
weak: 취약 지점의 위치가 담긴 배열 (len 1~15/원소 0~n-1)
dist: 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열
      (len 1~8 / 원소 1~100)
친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1
'''
from itertools import permutations
def solution(n, weak, dist):
    answer = n
    wlen, dlen = len(weak), len(dist)
    weak.extend([ele + n for ele in weak])  # 1차원 배열로 만들기
    cases = list(permutations(dist, dlen))  # permutatoin (완전 탐색)
    for idx in range(wlen):                 
        new_range = weak[idx:idx + wlen]    # weak 출발점 변경
        for case in cases:
            num, count = 0, 1
            poss_dist = new_range[0] + case[num]    # 이동가능 거리
            for weakp in new_range:        
                if weakp > poss_dist:       # 이동가능 거리를 지날 경우
                    count += 1
                    if count > dlen:        # 모든 dist를 사용했을 때
                        break
                    num += 1
                    poss_dist = weakp + case[num]
            answer = min(answer, count)
    if answer > dlen:
        answer = -1
    return answer
'''
import itertools
#1,2,7,8,9,16,17,18,19,20,21,25 통과 나머지 런타임 에러
def solution(n, weak, dist):
    answer = float('inf')
    weak_size = len(weak)

    #시계방향 탐색이 가능하도록 
    for i in range(len(weak)-1):
        weak.append(weak[i]+n)
    
    
    #dist로 순열 만들기
    dist_per = list(itertools.permutations(dist,len(dist))) 
    
    for per in dist_per:
        for i in range(weak_size):
            start = weak[i]
            end = weak[i+weak_size-1]
            for j in range(len(dist_per)):
                # 친구 이동
                start += per[j]  

                # 모든 지점 점검 마쳤을 경우
                if start >= end :
                    answer = min(answer, j+1)
                    break

                # 점검을 마치지 않았지만 더이상 이동할 수 없으면
                # 다음 지점으로 이동
                for z in range(i+1, i+weak_size): 
                    if weak[z] > start : 
                        start = weak[z]
                        break


            if answer == float('inf'):
                return -1
    
    
    return answer
'''
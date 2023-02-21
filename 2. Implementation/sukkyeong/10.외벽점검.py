# 외벽점검을 위해 보내야하는 친구의 최소값
from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1  # 최대값으로 초기화
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)  # 선형으로 표현하기 위해 n을 추가

    for start in range(length):
        for friends in permutations(dist, len(dist)):  # 모든 친구들에 대한 순열
            count = 1  # 투입된 친구 수
            position = weak[start] + friends[count-1]  # 시작점 설정
            for index in range(start, start+length):
                if position < weak[index]:  # 다음 지점까지 이동 불가능하면
                    count += 1  # 친구 추가 투입
                    if count > len(dist):  # 더 이상 투입 불가능하면
                        break
                    position = weak[index] + friends[count-1]  # 다음 친구의 시작점 설정
            answer = min(answer, count)  # 최소 친구 수 갱신
    if answer > len(dist):  # 모든 친구 투입해도 불가능한 경우
        return -1
    return answer

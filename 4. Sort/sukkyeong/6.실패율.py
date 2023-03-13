'''
실패율 = 클리어하지 못한 플레이의 수 / 스테이즈에 도달한 플레이어 수
샐패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담긴 배열 리턴
N = 스테이지 개수, stage = 사용자가 현재 멈춰있는 스테이지 번호가 담긴 배열
'''


def solution(N, stages):
    result = {}
    total = len(stages)
    for stage in range(1, N+1):
        if total != 0:
            count = stages.count(stage)
            result[stage] = count / total
            total -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)

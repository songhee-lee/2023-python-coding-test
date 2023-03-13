"""
- 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
- 실패율 높은 순으로 스테이지 번호 정렬
"""

def solution(N, stages):
    answer = []
    p = len(stages) # 스테이지 통과한 인원
    
    for i in range(1, N+1):
        if p <= 0 :     # 스테이지 통과한 사람이 없는 경우
            answer.append((i, 0))
            continue
        fail = stages.count(i)  # 실패한 유저의 수
        answer.append((i, fail / p))    # 실패율 기록
        p -= fail 
        
    answer = sorted(answer, key=lambda x: (-x[1], x[0]))
    print(answer)
    return [ a[0] for a in answer ]
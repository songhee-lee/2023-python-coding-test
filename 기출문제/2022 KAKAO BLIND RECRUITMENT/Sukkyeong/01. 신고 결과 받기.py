'''
게시판 불량 이용자 신고
한번에 한명 신고, 한명에게 최대 1번 가능
k번 이상 신고된 유저는 게시판 이용 정지
신고한 모든 유저에게 정지 사실 메일 발송

'''
# collections' 모듈에서 'defaultdict' 함수를 사용하여 딕셔너리를 초기화
from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    # 중복 제거
    report = list(set(report))

    # defaultdict을 사용하여 빈 set과 0으로 초기화된 딕셔너리 생성
    user = defaultdict(set)
    cnt = defaultdict(int)

    # 각 신고마다 신고자와 피신고자의 정보를 저장합니다.
    for r in report:
        a, b = r.split()
        user[a].add(b)  # a가 b를 신고했다는 정보를 추가
        cnt[b] += 1     # b를 신고한 횟수를 1 증가

    # 각 사용자마다 신고당한 횟수를 계산하여 리스트에 추가
    for i in id_list:
        result = 0
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)

    # 결과 리스트 반환
    return answer

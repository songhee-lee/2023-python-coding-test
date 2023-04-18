""" 
- 유저에 대해 신고 (유저당 1회만 적용됨)
- 신고했고 정지된 ID에 대해 리턴

- 유저 1000명
- 신고 건수 200,000

*** (유저, 신고당한 유저) 튜플을 정렬해서, 개수만 세는 방법으로도 해보기
"""
from collections import defaultdict
def solution(id_list, report, k):
    report = set(report)    # 동일한 신고 건수 제외
    
    # 유저별 신고 대상 저장
    users_report = defaultdict(set)   
    users_caution = defaultdict(int)    # 유저별 신고 건수
    for r in report:
        user, other = r.split()
        users_report[user].add(other)
        users_caution[other] += 1
    
    # 신고 대상자 확인
    stop_list = set()
    for user in id_list:
        if users_caution[user] >= k:
            stop_list.add(user)
    
    answer = [ len(users_report[user])-len(users_report[user]-stop_list) for user in id_list]
    return answer
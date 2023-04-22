from collections import defaultdict

# sol 1 - My sol
def solution(id_list, report, k):
    users = defaultdict(list) # key: 유저 ID, value: [신고한 ID]
    reported_users = defaultdict(int) # key: 신고당한 ID, value: 횟수
    ret = defaultdict(int) # key: 정지 당한 ID, value: 처리 결과 메일 받은 횟수
    
    # 딕셔너리 정보 초기화
    for id in id_list:
        users[id] = []
        reported_users[id] = 0
        ret[id] = 0
        
    
    for string in report:
        # 유저 ID, 유저가 신고한 ID
        user_id, reported_id = string.split(" ")
        
        # 신고한 ID 리스트에 없는 경우
        # 중복으로 신고한 ID 제외 처리
        if reported_id not in users[user_id]:
            users[user_id].append(reported_id) # 추가
            reported_users[reported_id] += 1 # 신고받은 횟수 1 증가시킴
            

    # 각 유저별로 처리 결과를 받기 위해 
    for user in users.keys():
        for id in reported_users.keys(): # 신고당한 유저 ID
            # 신고받은 횟수가 k번 이상
            # 해당 유저가 신고한 기록이 있다면 
            if reported_users[id] >= k and id in users[user]:
                # 처리 결과 갱신
                ret[user] += 1
    
    # 각 유저가 받은 메일 수를 반환하면 된다.
    # 따라서 딕셔너리의 values를 리스트로 변환하여 반환
    return list(ret.values())

# sol 2 - 최적화
def solution(id_list, report, k):
    answer = []
    report = list(set(report)) # 중복 신고 제거
    users = defaultdict(set) # user별 신고한 id 저장(key: user_id, value: 신고당한 id 목록)
    reported_cnt = defaultdict(int) # user별 신고당한 횟수 저장
    
    for r in report:
        # 신고자 id, 신고당한 id
        user_id, reported_id = r.split() 
        
        # 신고자가 신고한 id 추가
        users[user_id].add(reported_id)
        
        # 신고당한 id의 신고받은 횟수 추가
        reported_cnt[reported_id] += 1
    
    for id in id_list:
        ret = 0
        # user별 신고한 id 목록을 순회하며
        for user in users[id]:
            # 신고당한 횟수가 k번 이상이면
            if reported_cnt[user] >= k:
                # 처리 결과 메일을 받은 횟수 1 증가
                ret += 1
    
        answer.append(ret)
        
    return answer
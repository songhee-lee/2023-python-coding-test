from collections import defaultdict

def solution(enroll, referral, seller, amount):
    amount = [p * 100 for p in amount]
    profit = defaultdict(int) # 판매원의 총 이익
    parent = defaultdict(str) # 판매원의 추천인 정보(조직 구조)
    
    # 총 이익 초기화
    for p in enroll:
        profit[p] = 0
    
    # 조직 구조 초기화
    for e, r in zip(enroll, referral):
        parent[e] = r
    
    # 이익 계산하기
    for i, s in enumerate(seller):
        to_parent = amount[i] // 10 # 추천인에게 분배할 이익
        profit[s] += amount[i] - to_parent # 자신의 이익 = 판매 이익 - 분배 이익
        
        while 1:
            s = parent[s] # 추천인 
            if s == '-' or to_parent == 0: # '-' 즉, center거나 줄 이익이 없으면 
                break # 종료
            else:
                profit[s] += to_parent - to_parent // 10 # 추천인의 이익 갱신
            to_parent //= 10 # 추천인의 추천인(다단계)
    
    # 총 이익 반환(단, enroll의 순서를 따른다.)
    return list(profit.values()) 
# 이모티콘의 할인율을 설정해야 한다.
# 10, 20, 30, 40% 중 하나가 될 수 있는데, 이는 조합으로 설정해야 하나?
from collections import defaultdict

def solution(users, emoticons):
    answer = []
    sale_ratio = [10, 20, 30, 40]
    n = len(emoticons)
    sale_comb = [0] * n
    
    def set_ratio(idx):
        if idx == n: # 모든 이모티콘 별 할인율 설정 완료
            service_join = 0 # 플러스 서비스 가입자 수
            total_price = 0 # 매출액
            for ratio, price in users:
                cur_spent = 0 # 현재 사용자가 이모티콘 구매에 지불한 금액
                for i, emoticon_price in enumerate(emoticons):
                    if sale_comb[i] >= ratio: # 이모티콘 할인율이 비율% 이상 이라면,
                        cur_spent += int(emoticon_price * (100 - sale_comb[i]) / 100) # 구매
                
                if cur_spent >= price: # 가격 이상의 돈을 구매에 사용한다면, 서비스에 가입
                    service_join += 1
                else: # 이모티콘 구매
                    total_price += cur_spent
            answer.append([service_join, total_price])
            return
        
        for ratio in sale_ratio:
            sale_comb[idx] = ratio
            set_ratio(idx + 1)
            
    set_ratio(0)
    
    return sorted(answer, key=lambda x: (-x[0], -x[1]))[0]
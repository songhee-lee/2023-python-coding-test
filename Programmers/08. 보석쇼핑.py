# 특정 범위의 보석을 모두 구매하되 특별히 아래 목적 달성
# 목적 : 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

# 보석을 하나 이상 포함하는 가장 짧은 구간 찾기
# 시작 진열대 번호, 끝 진열대 번호 리턴

'''
탐색 문제인듯?
 1 이상 100,000 이하 ==> O(n^2) 이상이면 안돼
 “모든 종류의 보석을 포함하는 구간" 여부 : 딕셔너리 자료구조
'''

from collections import defaultdict

def solution(gems):
    gems_len = len(gems)
    gems_kind = len(set(gems))
    gems_dict = defaultdict(lambda: 0)
    
    answer =[]

    start, end = 0,0
    
    while True:
        if start == gems_len:
            break
        if end == gems_len:
            break
        kind = len(gems_dict)
        
        #모든 보석 하나씩 포함
        if kind == gems_kind:
            answer.append([start, end])
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
                
            start += 1
            continue
            
        if kind != gems_kind:
            gems_dict[gems[end]] += 1
            end += 1
            continue
    #while 문 끝
    
    _max = float('inf')
    real_answer = []
    for i in answer:
        if _max > i[1]-i[0]:
            _max = i[1]-i[0]
            real_answer = [i[0]+1,i[1]]
    
    
    return real_answer
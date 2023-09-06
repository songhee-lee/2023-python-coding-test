# 후보 키의 최대 개수를 구해야 한다. → 후보 키가 될 수 있는 모든 조합을 구하면 된다.
# 유일성을 만족해야 한다. → 중복되는 값이 있다면 해당 키는 유일성 만족하지 못함.
# 최소성을 만족해야 한다. → 유일성의 조합에서 하나를 제외했을 때 유일성이 깨지면 만족 못한다. → 유일성의 조합으로만 이루어져야 한다?
# 최소성이란? 예시에서 학번으로 모든 학생을 구별할 수 있다. 그렇다면 [학번, 이름]으로 구별할 필요가 있을까? → 굳이 이름을 끼지 않아도 된다. 학번 자체만으로도 구별이 가능하기 때문이다.
# 즉, 최소성은 굳이 넣지 않아도 될 속성을 넣지 않은 것을 말한다.
from itertools import combinations
def solution(relation):
    n = len(relation[0])
    
    # 유일성을 만족하는 키를 찾는다.
    def unique():
        unique_key = []
        for key in candidate_key:
            main = []
            for r in relation:
                sub = []
                for c in key:
                    sub.append(r[c])
                main.append(tuple(sub))
            if len(set(main)) == len(relation):
                unique_key.append(key)
                
        return unique_key
    
    # unique_key_set을 list로 remove하면 실패.. set으로 변경해야 한다.
    # 최소성을 만족하는 키를 찾는다.
    def minimal():
        minimal_key_count = 0
        unique_key_set = set(unique_key)
        _len = len(unique_key)
        for i in range(_len - 1):
            for j in range(i + 1, _len):
                if len(unique_key[i]) == len(set(unique_key[i]) & set(unique_key[j])):
                    unique_key_set.discard(unique_key[j])
        # 실패.
        # while unique_key:
        #     minimal_key = unique_key_set.pop()
        #     idx = 0
        #     while idx < len(unique_key_set):
        #         key = unique_key_set[idx]
        #         if set(minimal_key) & set(key):
        #             unique_key_set.discard(key)
        #             continue
        #         else:
        #             idx += 1
                    
            # minimal_key_count += 1
        return len(unique_key_set)
    
    # 후보키 조합을 구한다.
    candidate_key = []
    for i in range(1, n + 1):
        candidate_key.extend(list(combinations(range(n), i)))
    
    
    unique_key = unique() # 유일성을 만족하는 키를 찾는다.
    candidate_key_count = minimal() # 후보키의 최대 개수
    
    return candidate_key_count
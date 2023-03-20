""" 
- 특정 키워드가 몇 개 포함되어 있는지 찾기
- ? 는 어떤 문자랑도 매치

** 아직 효율성 통과 못함
"""
import re

def solution(words, queries):
    answer = [0] * len(queries)
    
    qn = [ len(q) for q in queries ]    # 쿼리 단어 길이
    wn = [ len(w) for w in words ]      # 가사 단어 길이
    _queries = []
    for q in queries:
        w = ''
        for i in range(len(q)):
            if q[i] == '?':
                w += '[a-z]'
            else:
                w += q[i]
        _queries.append(w)

    for i, query in enumerate(_queries):
        for j, word in enumerate(words):
            if qn[i] != wn[j]:  # 두 단어의 길이가 다른 경우 pass
                continue
            
            # 단어 비교
            if re.sub(query, '', word) == '':
                answer[i] += 1
            
    return answer
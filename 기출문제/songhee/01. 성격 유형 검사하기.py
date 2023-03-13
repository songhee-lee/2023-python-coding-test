""" 
- 16가지 성격 유형
- 7가지 점수 (-3 ~ 3)
- 점수가 같으면  두 성격 유형 중 사전 순으로 빠른 성격 유형
- survey = (비동의, 동의 유형)
    -> 
"""

def solution(survey, choices):
    n = len(survey)
    result = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(n):
        score = choices[i]
        if score > 4:   # 동의
            result[survey[i][1]] += score-4
        elif score < 4: # 비동의
            result[survey[i][0]] += abs(4-score)
    
    answer = 'R' if result['R'] >= result['T'] else 'T'
    answer += 'C' if result['C'] >= result['F'] else 'F'
    answer += 'J' if result['J'] >= result['M'] else 'M'
    answer += 'A' if result['A'] >= result['N'] else 'N'
    
    return answer
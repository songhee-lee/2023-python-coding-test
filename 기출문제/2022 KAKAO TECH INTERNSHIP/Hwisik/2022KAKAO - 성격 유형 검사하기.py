'''
- 딕셔너리를 이용하여 각 성격 유형 저장(key: 성격 유형, value: 점수)
- 검사지와 선택지 동시에 순회하면서 해당되는 성격유형에 점수 저장
- 딕셔너리의 Items를 리스트로 변환하여 각 지푶마다 어떤 성격 유형이 점수가 더 높은지 확인
'''
# sol 1 - 초기 풀이
def solution(survey, choices):
    n = len(survey)
    # dic = { 'R' : 0, 'T' : 0, 'C' : 0, 'F': 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    dic = {
        1 : {
            'R' : 0,
            'T' : 0,
        },
        2 : {
            'C' : 0,
            'F' : 0,
        },
        3 : {
            'J' : 0,
            'M' : 0,
        },
        4 : {
            'A' : 0,
            'N' : 0,
        }
    }
    answer = ''
    
    for i in range(n):
        no_agree, yes_agree = survey[i][0], survey[i][1]
        choice = choices[i]
        score = 0
        if choice == 1 or choice == 7:
            score = 3
        elif choice == 2 or choice == 6:
            score = 2
        elif choice == 3 or choice == 5:
            score = 1
        
        if choice == 1 or choice == 2 or choice == 3:
            if no_agree == 'R' or no_agree == 'T':
                dic[1][no_agree] += score
            elif no_agree == 'C' or no_agree == 'F':
                dic[2][no_agree] += score
            elif no_agree == 'J' or no_agree == 'M':
                dic[3][no_agree] += score
            elif no_agree == 'A' or no_agree == 'N':
                dic[4][no_agree] += score
            # dic[no_agree] += score
        elif choice == 5 or choice == 6 or choice == 7:
            if yes_agree == 'R' or yes_agree == 'T':
                dic[1][yes_agree] += score
            elif yes_agree == 'C' or yes_agree == 'F':
                dic[2][yes_agree] += score
            elif yes_agree == 'J' or yes_agree == 'M':
                dic[3][yes_agree] += score
            elif yes_agree == 'A' or yes_agree == 'N':
                dic[4][yes_agree] += score
    
    for key in dic.keys():
        val = 0
        ret = 'Z'
        for subkey in dic[key].keys():
            if val < dic[key][subkey]:
                val = dic[key][subkey]
                ret = subkey
            elif val == dic[key][subkey]:
                if ret > subkey:
                    ret = subkey
        answer += ret
    return answer

# sol 2 - 재도전
def solution(survey, choices):
    # 성격 유형(딕셔너리)
    dic = { "R" : 0, "T" : 0, 
            "C" : 0, "F" : 0, 
            "J" : 0, "M" : 0, 
            "A" : 0, "N" : 0 
          }
    
    # 검사지와 선택지 동시에 순회
    for s, c in zip(survey, choices):
        # 약간 동의(5, 1점), 동의(6, 2점), 매우 동의(7, 3점)
        if c > 4:
            dic[s[1]] += c - 4 # 
            
        # 약간 비동의(3, 1점), 비동의(2, 2점), 매우 비동의(1, 3점)
        elif c < 4:
            dic[s[0]] += 4 - c
    
    # 딕셔너리 -> 리스트
    dic_to_list = list(dic.items())
    
    answer = ""
    
    # 2개 단위로 검사
    for i in range(0, 8, 2):
        f, s = dic_to_list[i], dic_to_list[i + 1]
        
        # 점수가 큰 쪽을 선택
        if f[1] < s[1]:
            answer += s[0]
        else:
            answer += f[0]
    
    return answer
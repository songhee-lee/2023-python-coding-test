'''
요구사항
    - 문자열을 1개 이상의 단위로 잘라서 압축하여 가장 짧게 표현할 수 있는 문자열 찾기
    - 찾은 문자열의 길이를 return
    => 어떻게 가장 짧게 표현할 수 있을까?
        : 반복되는 문자열 중 가장 긴 것을 단위로 자르면?
    잘라야 하는 단위는 동일해야 한다.
    예를 들어 2개 단위라면, 나머지 문자열도 모두 2개 단위로 자르던지, 자를 수 없다면 자르지 않도록 해야 한다.
    (조심)예시 3. s = "abcabcdede"
'''

def solution(s):
    max_unit = len(s) // 2 # 최대로 압축할 수 있는 단위
    min_len = len(s) # 압축을 전혀 할 수 없는 경우, s의 길이가 답이 된다.
    
    # 1 <= unit <= max_unit
    for unit in range(1, max_unit + 1): # 압축 단위를 1부터 시작
        idx = 0 # 문자열 슬라이싱에 사용하는 인덱스(항상 왼쪽부터 살펴본다)
        n = len(s) # 문자열의 길이
        
        while idx < len(s) - unit + 1:
            cur = s[idx:idx + unit] # 압축할 문자열 
            idx += unit # 다음 문자열을 살펴보기 위해 idx 증가시킨다.
            
            count = 0 # 압축 문자열이 반복되는 횟수
            while idx < len(s) - unit + 1:
                target = s[idx:idx + unit] # cur 이후의 문자열
                
                if cur == target: # 만약 압축이 가능하다면
                    count += 1 # 반복 횟수 1 증가시킨다.
                    idx += unit # 다음 인덱스를 확인한다.
                else: # 서로 다른 문자열이라면
                    break
                
            if count > 0: # 압축 가능한 문자열이 있다면
                n -= unit * count # (단위 * 반복 횟수) = (압축할 문자열의 길이 * 반복 횟수)
                
                # 반복횟수 비교가 중요하다.
                # ex) abcabcabc 일 때 단위가 3이라고 가정하면,
                # count = 3이므로 3abc가 된다. => 즉, n -= 3(unit) * 2 
                # count는 3인데 왜 2를 곱하나? -> cur을 count로 세지 않기 때문이다.
                # 따라서, 그에 대한 처리가 아래의 코드이다.
                
                if count < 9: # 9가 포함이 된다면 cur을 세지 않음을 포함하므로, 실질적으로 반복된 횟수는 10이다. 따라서, count = 9일 때는 10의 자릿수인 2를 더해야한다. 따라서, 9 미만의 범위를 갖는다.
                    n += 1
                elif count < 99: # 10<= count < 99 -> 99를 포함하지 않는 이유는 위의 설명과 같다.
                    n += 2
                elif count < 999:
                    n += 3
                else: n += 4
            min_len = min(min_len, n) # 압축을 완료했으므로, 가장 짧은 압축 문자열의 길이를 찾는다.
    
    answer = min_len
    return answer # 가장 짧은 압축 문자열의 길이를 return.
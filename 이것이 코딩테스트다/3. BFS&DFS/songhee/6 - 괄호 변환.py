"""
문제> 올바른 괄호 문자열로 반환해 리턴
    - ( 개수와 ) 개수가 같으면 '균형잡힌 괄호 문자열'
    - ( )의 짝도 모두 맞으면 '올바른 괄호 문자열'

    - 균형잡힌 괄호 문자열의 경우 올바른 괄호 문자열로 변환 가능
"""

def check(p):
    # 올바른 문자열은 항상 open ( 개수가 close ) 보다 많거나 같음

    bracket = 0
    for x in p:
        bracket = (bracket+1) if x == '(' else (bracket-1)
        
        if bracket < 0:
            return False
    return True

def split(p):
    # open ( close ) 개수가 같으면 균형잡힌 문자열
    o, c = 0, 0
    for x in p:
        if x == '(' :
            o += 1
        else :
            c += 1
        
        if c == o :
            return o, c
    return p[:o+c], p[o+c:]
        
def solution(p):
    
    # 1. 빈 문자열인 경우
    if not p :
        return ''
    
    # 2. 올바른 괄호 문자열인지 확인
    if check(p):
        return p

    # 3. 올바른 문자열로 변환
    # 균형잡힌 문자열 u, v로 분리
    u, v = split(p)
    
    # 3-1. u가 올바른 문자열이면 v 변환 후 반환
    if check(u):
        return u + solution(v)
    
    # 4. u가 올바른 괄호문자열 아니면
    else:
        tmp = "(" + solution(v) + ")" # 4-1, 4-2, 4-3
        
        # 4-4. u 앞뒤 자르고 toggle
        tmp_u = ''.join( [ '(' if x == ')' else ')' for x in u[1:-1]])
    
    return tmp + tmp_u

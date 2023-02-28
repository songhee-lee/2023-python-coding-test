
# 균형잡힌 : '(' 개수 == ')' 개수
# 올바른 : 균형잡힌 and '(' ')' 짝이 맞음
from collections import deque
import copy

# 주어진 문자열을 두 개로 나누는 함수 : u,v
def seperate(brackets):
    if not brackets : return deque()
    bracket = copy.deepcopy(brackets)
    u = deque()
    v = deque()
    left, right = 0,0 # left:'('의 개수, right:')'개수
    
    while bracket:
        # u : 균형잡힌 괄호 문자열로 더이상 나눌 수 없는 균형잡힌 괄호 문자열
        u.append(bracket.popleft())
        if u[-1] == '(' : left+=1
        else : right+=1
        if left and right and left==right:
            v = bracket    # v : 나머지 문자열
            break

    # u가 올바른 괄호 문자열이 아닌 경우
    if u and not check(u):
        # u의 앞 뒤 문자를 제거한다
        if len(u) == 2: return deque('()')+seperate(v)
        u.popleft()
        u.pop()
        # 나머지 u의 괄호 문자열 방향들을 뒤집고, 앞 뒤로 '(', ')'를 이어붙인 다음
        # v 문자열의 seperate 함수 결과를 이어 붙인다
        return deque('(')+Reverse(u)+deque(')')+seperate(v)
    
    return deque(u)+seperate(v)
        
# 괄호 문자열의 괄호 방향을 뒤집는 함수
def Reverse(brackets):
    bracket=copy.deepcopy(brackets)
    Reversed = []
    while bracket:
        b = bracket.popleft()
        if b == '(' : Reversed.append(')')
        else : Reversed.append('(')
    return deque(Reversed)
 
# 올바른 괄호 문자열인지 확인하는 함수
def check(brackets):
    if brackets:
        bracket = copy.deepcopy(brackets)
        if bracket.popleft() == '(' : left = 1
        else : return False
        while bracket:
            if bracket.popleft() == '(' : left+=1
            else : left-=1
        if left == 0 : return True
        else : return False

def solution(p):
    return ''.join(seperate(deque(p)))
    
print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))
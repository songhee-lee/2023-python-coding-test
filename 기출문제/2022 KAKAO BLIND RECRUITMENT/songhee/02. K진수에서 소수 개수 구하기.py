""" 
- 0P0
- P0
- 0P
- P : 각 자릿수에 0을 포함하지 않는 소수

** 조건에 맞는 P를 찾고, 소수판별하기
"""
def is_Prime(number):
    if number == 1:
        return False
    
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def solution(n, k):
    
    # k진수 구하기
    n_k = ''
    while n > 0:
        n_k += str(n % k)
        n //= k
    
    n_k = ''.join(reversed(n_k))
    
    # 조건에 맞는 P찾기
    cand = n_k.split('0')

    # 소수 판별
    answer = 0
    for number in cand:
        if number == '': continue
        if is_Prime(int(number)):
            answer += 1
            
    return answer
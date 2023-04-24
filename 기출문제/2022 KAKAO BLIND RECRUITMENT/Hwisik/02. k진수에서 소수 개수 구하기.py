'''
- 에라토스테네스의 체 _max값을 어떻게 설정? -> 필요 없음 ;0;, 범위 설정이 불가능함, 진법 변환시에 최대로 나올 수 있는 수가 뭔지 모름
-> 단순 소수 판별해야 함.

- 소수의 조건
    - 0P0 / P0 / 0P / P 
    - 단, P는 0을 포함하지 않는 소수

- return 조건에 맞는 소수의 개수 
'''

# sol 1 - My sol
# 진법 변환
def to_k(n, k):
    ret = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        ret += str(mod)
        
    return ret[::-1] # str 타입

def solution(n, k):
    answer = 0
    
    # 문제의 조건을 종합하면, 0을 기준으로 나누면 됨
    splited = to_k(n, k).split("0")
    
    # P에 대하여,
    for p in splited:
        flag = False # 소수 판별 플래그
        # 빈 문자열이 아니고
        # 각 자릿수에 0이 없고
        # 1이 아니라면(1은 소수가 아니기 때문)
        if p != '' and '0' not in p and p != '1':
            int_p = int(p) # int 형변환
            
            # 소수 판별
            for i in range(2, int(int_p ** 0.5) + 1):
                if int_p % i == 0: # 자기 자신 이외 약수를 가지면
                    flag = True # 소수가 아니다.
            # 소수라면
            if not flag:
                answer += 1 # 카운트 + 1
            
    return answer


# sol 2 - 최적화
# 진법 변환
def k_base_conversion(n, k):
    ret = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        ret += str(mod)
        
    return ret[::-1] # str 타입
    
# 소수 판별
def isPrime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

def solution(n, k):
    answer = 0
    
    # 문제의 조건을 종합하면, 0을 기준으로 나누면 됨
    converted = k_base_conversion(n, k).split("0")
    
    for p in converted:
        if p != '':
            if isPrime(int(p)):
                answer += 1
    
    return answer
'''
- 라이언은 어피치를 가장 큰 점수 차이로 이기려고 함
- n발의 화살을 알맞게 조합해야 한다.
- 라이언의 n발의 화살을 (10점 ~ 0점까지) 순서대로 리스트에 담아 return
- 우승 X or 비기기 -> return [-1]
- 가장 큰 점수 차이로 이길수 있는 경우의 수가 여러 개 -> 가장 낮은 점수를 맞힌 경우를 return

- 조합 계산에서, dfs 말고 combinations_with_replacement를 사용해도 된다.
'''

# test case 8, 18 틀림
from collections import defaultdict

answer = []
_max = 0 # 라이언과 어피치 사이의 가장 큰 점수 차이를 저장
dic = defaultdict(list) # 라이언과 어피치 사이의 점수 차이를 저장

# 라이언, 어피치의 점수 계산
def calc_score(n, a, r):
    # 어피치의 점수, 라이언의 점수
    sum_a, sum_r = 0, 0
    
    # 0점부터 10점까지
    for i in range(11): 
        if a[i] == 0 and r[i] == 0: # 둘 다 i점에 단 하나의 화살도 맞추지 못하면, 어느 누구도 점수를 얻지 않는다.
            continue
        elif a[i] >= r[i]: # 어피치가 더 많이 맞춤
            sum_a += (10 - i)
        else: # 라이언이 더 많이 맞춤
            sum_r += (10 - i)
    
    return (sum_a, sum_r)    

# 라이언이 맞출 수 있는 화살의 조합 구하기
def dfs(n, cnt, idx, a, r):
    global answer
    global _max

    # 화살 n개를 모두 사용했다면
    if cnt == n:
        sum_a, sum_r = calc_score(n, a, r) # 어피치, 라이언의 점수를 계산
        # 라이언의 점수가 더 크다면
        if sum_r > sum_a:
            # 가장 큰 점수차이를 갖는 경우를 저장 & 가장 큰 점수 차이가 여러 번 있을 수 있으므로, 
            if _max <= (sum_r - sum_a):
                _max = sum_r - sum_a # 점수 차이 갱신
                dic[_max].append(list(r)) # 가장 큰 점수 차이를 갖는 경우의 수를 저장
                return 
    
    # 0점부터 10점까지
    for i in range(idx, 11):
        if a[i] >= r[i]: # 어피치가 i점을 더 많이 or 같게 맞췄다면
            r[i] += 1 # 라이언이 i점에 맞춘다.
            dfs(n, cnt + 1, i, a, r)
            r[i] -= 1 # 라이언이 i점에 맞추지 않는다. -> 다른 조합을 위해서 원상복구
            
def solution(n, info):
    rian = [0] * 11 # 라이언이 맞춘 점수 조합
    dfs(n, 0, 0, info, rian)
    
    # 실패 코드
    # print(dic)
    # dic[_max].sort(key=lambda x: x[::-1])
    
    # 가장 낮은 점수를 더 많이 맞힌 경우를 return 해야 한다.
    # 따라서, 가장 큰 점수 차이를 갖는 경우 중, 가장 낮은 점수의 개수(key=lambda x: x[::-1])를 기준으로 오름차순 정렬을 한다.
    # 오름차순 정렬을 수행했으니, 맨 뒤에 값을 가져온다.
    # 만약, 가장 큰 점수 차이를 갖는 경우가 없다면, [-1]을 return 한다.
    return sorted(dic[_max], key=lambda x: x[::-1])[-1] if dic[_max] else [-1]
'''
- 먼저, stages 리스트를 오름차순 정렬한다.(계산 쉽게 하기 위해서)
- 각 스테이지에 머물러있는 사람의 수를 리스트에 저장한다.
- 스테이지 1부터 N까지 순회하면서, 스테이지에 도달한 플레이어 수와 클리어하지 못한 플레이어를 구한다.
- '클리어 X 사람 수 / 스테이지에 도달한 플레이어 수'를 리스트에 저장한다.
- 만약, 스테이지에 도달한 플레이어가 없다면 리스트에 0을 저장한다.
- 문제의 조건에 맞게 리스트를 return한다.
'''
# 그나마 효율적
def solution(N, stages):
    answer = [] # 반환 배열
    fail_rate = [] # 실패율 저장 (스테이지, 실패율)
    stage_count = [0] * (N + 2) # 각 스테이지 당 사람의 수
    
    # 오름차순 정렬
    stages.sort() 
    
    # 각 스테이지 당 사람의 수를 저장
    for stage in stages:
        stage_count[stage] += 1

    # 스테이지 순회(1 ~ N)
    for i in range(1, N + 1):
        total = sum(stage_count[i:]) # i번 스테이지에 도달한 플레이어 수
        not_clear = stage_count[i] # i번 스테이지에 도달했으나 클리어하지 못한 플레이어 수
        
        
        if total == 0: # 도달한 플레이어가 없다.
            fail_rate.append((i, 0)) # 실패율은 0
        else:
            fail_rate.append((i, not_clear / total)) # 실패율 저장
    
    # 실패율 내림차순, 스테이지 번호 오름차순 정렬
    for key in sorted(fail_rate, key=lambda x:(-x[1], x[0])):
        answer.append(key[0]) # 스테이지 번호만 저장
           
    return answer

# 비효율적
def solution(N, stages):
    answer = []
    stages.sort()
    rate_of_fail = []
    for step in range(1, N + 1):
        not_clear, total = 0, 0
        for stage in stages:
            if stage == step: 
                not_clear += 1
            if stage >= step: 
                total += 1 
        if total == 0:
            rate_of_fail.append((step, 0))
        else:
            rate_of_fail.append((step, not_clear / total))
    rate_of_fail.sort(key=lambda x:(-x[1], x[0]))
    for x, y in rate_of_fail:
        answer.append(x)
    return answer

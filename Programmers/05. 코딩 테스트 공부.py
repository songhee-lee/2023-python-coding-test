# 알고력 >= 0, 코딩력 >= 0 (정수)
# 문제를 풀기 위해 일정 이상의 알고력, 코딩력

# 알고력 높이기 : 알고리즘 공부, 1을 위해 1시간 필요
# 코딩력 높이기 : 코딩 공부, 1을 위해 1시간 필요
# 현재 풀수 있는 문제 풀기 (각 문제마다 정해져있음)
# 문제를 하나 푸는 데 문제가 요구하는 시간 필요 / 같은 문제 여러 번 가능

# 주어진 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 "최단시간 구하기"

# // 뒤에 숫자는 정확성 테스트 케이스 제한사항
# 0 <= alp : 초기의 알고력  <=150  // 20
# 0 <= cop : 초기의 코딩력  <=150  // 20
# 1 <= problems : 문제의 정보를 담은 2차원 정수 배열 <= 100 // 6
#           [필요한 알고력, 필요한 코딩력, 증가하는 알고력<=30 // 20, 증가하는 코딩력<=30, 풀이 시간<=100 // 10]

# 모든 문제들을 1번이상씩 풀 필요 없음

# 정확성 테스트 10초
# 효율성 테스트 : 언어별로 작성된 정답 코드의 실행 시간의 적정 배수


def solution(alp, cop, problems):
    max_alp = max(max([p[0] for p in problems]) - alp + 1, 1)
    max_cop = max(max(p[1] for p in problems) - cop + 1, 1)
    #problems.sort(key=lambda x: (min(x[0], max_alp) + min(x[1], max_cop)))
    dp = [[i + j for j in range(max_cop)] for i in range(max_alp)]

    for need_alp, need_cop, alp_up, cop_up, dist in problems:
        need_alp = max(need_alp - alp, 0)
        need_cop = max(need_cop - cop, 0)

        for a in range(need_alp, max_alp):
            for c in range(need_cop, max_cop):
                x = min(a + alp_up, max_alp - 1)
                y = min(c + cop_up, max_cop - 1)

                if dp[x][y] > dp[a][c] + dist:
                    dp[x][y] = dp[a][c] + dist

    return dp[-1][-1]

# def solution(alp, cop, problems):
#     #목표치 알고력, 코딩력
#     max_alp, max_cop = [0, 0]  
#     for problem in problems:
#         max_alp = max(max_alp, problem[0])
#         max_cop = max(max_cop, problem[1])
    
#     #처음 설정된 알고력, 코딩력이 최종 목표값보다 높을 경우
#     alp = min(alp, max_alp)
#     cop = min(cop, max_cop)

#     dp = [[float('inf')] * (max_cop+2) for _ in range(max_alp+2)]
    
#     dp[alp][cop] = 0
    
#     for i in range(alp, max_alp+1):
#         for j in range(cop, max_cop+1):
#             #공부하기
#             dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
#             dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            
#             for m in range(len(problems)):
#                 #현재 알고력과 코딩력이 문제를 해결할 수 있는 조건을 넘었을 경우
#                 if i >= problems[m][0] and j >= problems[m][1] :
                    
#                     #알고력과 코딩력이 목표치를 넘었을 경우
#                     if i + problems[m][2] > max_alp and j+problems[m][3] > max_cop:
#                         dp[max_alp][max_cop] = min(dp[max_alp][max_cop]), dp[i][j[ + problems[m][4]]]
#                     #알고력이 목표치를 넘었을 경우
#                     elif i + problems[m][2] > max_alp:
#                         dp[max_alp][j+problems[m][3]] = min(dp[max_alp][j+problems[m][3]], dp[i][j]+problems[m][4])
                        
#                     #코딩력이 목표치를 넘겼을 경우
#                     elif j + problems[m][3] > max_cop:
#                         dp[i+problems[m][2][max_cop] = min(dp[i]+problems[m][2][max_cop], dp[i][j]+problems[m][4])
#                     #목표치에 도달하지 못 한 경우
#                     elif i + problems[m][2] <= max_alp and j+problems[m][3] <= max_cop:
#                            dp[i+problems[m][2]][j+problems[m][3]] = min(dp[i+problems[m][2]][j+problems[m][3]], dp[i][j]+problems[m][4])
                                                                                             
                                                                                
#                                                                                         return dp[max_alp][max_cop]

'''dist 런타임 에러'''
'''    
import heapq

def solution(alp, cop, problems):

    #목표치 알고력, 코딩력
    # max_alp, max_cop = [0, 0]  
    # for problem in problems:
    #     max_alp = max(max_alp, problem[0])
    #     max_cop = max(max_cop, problem[1])
    max_alp, max_cop = max(x[0] for x in problems), max(x[1] for x in problems)
    #problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

    #처음에 목표치 알고력,코딩력을 넘는 경우가 있음
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    #다익스트라용 2차원 배열 
    dist = [[float('inf')] * (max_cop+1) for _ in range(max_alp+1)]
        
    dist[alp][cop] = 0
    queue = [[0, alp, cop]]

    while queue:
        cur_d, cur_alp, cur_cop = heapq.heappop(queue)
        
        if cur_alp >= max_alp and cur_cop >= max_cop:
            return cur_d
        
        if dist[cur_alp][cur_cop] <= cur_d:
            for need_alp, need_cop, alp_up, cop_up, distance in problems:
                
                next_alp, next_cop = min(150, cur_alp + need_alp), min(150, cur_cop + need_cop)
                if cur_alp >= need_alp and cur_cop >= need_cop and cur_d + distance < dist[next_alp][next_cop]:
                    dist[next_alp][next_cop] = cur_d + distance
                    heapq.heappush(queue, (cur_d + distance, next_alp, next_cop))
                    
    return dist[-1][-1]
'''                    
                    
'''dp 참고'''
'''
def solution(alp, cop, problems):
    max_alp_req, max_cop_req = [0, 0]  # 목표값
    
    for problem in problems:
        max_alp_req = max(max_alp_req, problem[0])
        max_cop_req = max(max_cop_req, problem[1])
    
    dp = [[float('inf')] * (max_cop_req+1) for _ in range(max_alp_req+1)]
    
    alp = min(alp, max_alp_req)  # 둘중 하나라도 목표값을 넘어가면 안된다.
    cop = min(cop, max_cop_req)
    
    dp[alp][cop] = 0  # dp[i][j]의 의미 : 알고력 i, 코딩력 j을 도달 할 수 있는 최단시간
    
    for i in range(alp, max_alp_req+1):
        for j in range(cop, max_cop_req+1):
            if i < max_alp_req:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop_req:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i+alp_rwd, max_alp_req)  # 둘중 하나라도 목표값을 넘어가면 안된다.
                    new_cop = min(j+cop_rwd, max_cop_req)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
                    
    return dp[max_alp_req][max_cop_req]

'''

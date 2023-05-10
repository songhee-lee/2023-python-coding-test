'''
돌다리 건너는 경우의 수 출력

DP로 풀이하기 위해 점화식을 도출한다.
DP[i][j][0] = sum(DP[v][j-1][1] , 0<= v < i)
DP[i][j][1] = sum(DP[v][j-1][0] , 0<= v < i)
여기서, DP[i][j][k]에서 i가 의미하는것은 현재 위치, j가 의미하는것은 현재 문자열이 두루마리의 몇번째에 적힌 문자열인지, k가 의미하는 것은 0일땐 악마의 돌다리, 1일땐 천사의 돌다리이다.
점화식을 이용하여 전체 경우의 수를 구한 전체 DP테이블에서 두루마리의 마지막 문자까지 간 경우의 수들만 더해주면 된다.
'''

import sys  # sys 모듈 import

# 입력 값을 처리하기 위한 함수 정의


def input(): return sys.stdin.readline().rstrip()


# 첫번째 문자열 값
target = input()

# 두번째 문자열 값
s1 = input()

# 세번째 문자열 값
s2 = input()

# dp 배열 초기화
dp = [[[0] * 2 for _ in range(len(target))] for _ in range(len(s1))]

# 첫번째 열 초기화
for i in range(len(s1)):
    if s1[i] == target[0]:
        dp[i][0][0] = 1
    if s2[i] == target[0]:
        dp[i][0][1] = 1

# dp 배열 갱신
for i in range(len(s1)):
    for j in range(1, len(target)):
        if s1[i] == target[j]:
            for k in range(i):
                dp[i][j][0] += dp[k][j-1][1]

        if s2[i] == target[j]:
            for k in range(i):
                dp[i][j][1] += dp[k][j-1][0]

# dp 배열의 값을 모두 더해서 answer에 저장
answer = 0
for i in range(len(s1)):
    answer += (dp[i][len(target)-1][0] + dp[i][len(target)-1][1])

# 결과 출력
print(answer)

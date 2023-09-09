"""
선수과목 있는 과목은 선수과목을 먼저 이수해야 해당 과목을 이수할 수 있다.
모든 과목에 대해 각 과목을 이수하려면 최소 몇 학기가 걸리는지 계산하기

1 <= 과목의 수 N <= 1000
1 <= 선수 조건의 수 M <= 500,000

- 풀이 1, 2 모두 sys.stdin.readline 사용해야 시간초과 안남.
"""

"""풀이 1"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
prerequisite = [[] for _ in range(N+1)]
for _ in range(M) :
    # a가 b의 선수과목
    a, b = map(int, input().split())
    prerequisite[b].append(a)
prerequisite = sorted([(i, p) for i, p in enumerate(prerequisite)], key=lambda x: len(x))[1:]

# dp[i] : i번째 과목을 이수하는데 걸리는 최소 학기
# dp[i] = 선수과목 중 가장 오래 걸리는 학기 + 1
dp = [1] * (N+1)
for i, pre in prerequisite :
    if pre :
        dp[i] = max([dp[p]+1 for p in pre])

print(*dp[1:])


"""풀이 2"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
prerequisite = []
for _ in range(M) :
    # a가 b의 선수과목
    a, b = map(int, input().split())
    prerequisite.append((a, b))

# 1) 선수 과목의 번호는 항상 A < B 이다
# 2) A의 이수학기 수가 B보다 크다면 B는 A의 이수학기+1로 변경된다.
prerequisite.sort()
answer = [1] * (N+1)
for a, b in prerequisite :
    if answer[b] <= answer[a] :
        answer[b] = answer[a] + 1

print(*answer[1:])
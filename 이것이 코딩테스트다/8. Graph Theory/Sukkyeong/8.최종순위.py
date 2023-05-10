'''
n개의 팀이 참가
1~n번까지 번호가 있음
작년에 비해 상대 순위가 바뀐 팀의 목록만 발표

'''

from collections import deque
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    inDegree = [0 for _ in range(n + 1)]
    queue = deque()
    answer = []
    flag = 0

    team = list(map(int, sys.stdin.readline().rstrip().split()))

    # 그래프 생성
    for j in range(n - 1):
        for k in range(j + 1, n):
            graph[team[j]].append(team[k])
            inDegree[team[k]] += 1

    m = int(sys.stdin.readline())

    # 우선순위 변경이 일어날 경우 그래프 업데이트
    for j in range(m):
        first, second = map(int, sys.stdin.readline().rstrip().split())
        flag = True

        for k in graph[first]:
            if k == second:
                graph[first].remove(second)
                inDegree[second] -= 1
                graph[second].append(first)
                inDegree[first] += 1
                flag = False

        if flag:
            graph[second].remove(first)
            inDegree[first] -= 1
            graph[first].append(second)
            inDegree[second] += 1

    # 위상정렬 수행
    for j in range(1, n + 1):
        if inDegree[j] == 0:
            queue.append(j)

    # 위상정렬 결과가 여러개이거나 불가능할 경우 처리
    if not queue:
        print("IMPOSSIBLE")
        continue

    result = True
    while queue:
        if len(queue) > 1:
            result = False
            break

        tmp = queue.popleft()
        answer.append(tmp)
        for j in graph[tmp]:
            inDegree[j] -= 1
            if inDegree[j] == 0:
                queue.append(j)
            elif inDegree[j] < 0:
                result = False
                break

    if not result or len(answer) < n:
        print("IMPOSSIBLE")
    else:
        print(*answer)

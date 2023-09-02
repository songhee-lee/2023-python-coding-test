"""
A가 B의 친구가 되려면 두 사람이 친구거나, A와 친구이고 B와 친구인 C가 존재하면 된다.
가장 친구의 수가 많은 사람의 친구 수 구하기
=> A와 거리가 1 또는 2인 노드 개수 구하기
"""
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().strip()) for _ in range(N)]

cnt = [0] * N
for i in range(N) :
    for j in range(N) :
        if i == j : continue

        is_friend = 0
        # i와 j가 친구인 경우
        if graph[i][j] == 'Y' :
            is_friend = 1
        # i와 k가 친구고, k와 j가 친구인 경우
        else :
          for k in range(N) :
              if graph[i][k] == 'Y' and graph[k][j] == 'Y' :
                  is_friend = 1
                  break
        cnt[i] += is_friend

print(max(cnt))
    
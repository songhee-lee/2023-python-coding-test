from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
array = [list(map(int, stdin.readline().split())) for _ in range(n)]

chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            houses.append((i, j))
        elif array[i][j] == 2:
            chickens.append((i, j))

ans = 100000
alive_chicken = list(combinations(chickens, m))

for alive in alive_chicken:
    tmps = 0
    for house in houses:
        tmp = 1000000
        for chicken in alive:
            tmp = min(tmp, abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
        tmps += tmp
    ans = min(ans, tmps)

print(ans)

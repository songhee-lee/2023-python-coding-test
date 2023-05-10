'''
주어진 n개의 행성을 모두 연결하는데 드는 최소 비용을 구해야 합니다.
이를 위해서는 모든 행성 간의 거리를 계산하고, 최소 스패닝 트리를 구하면 됩니다.

먼저 행성 간의 거리를 계산하는 부분입니다. 이를 위해 x, y, z 좌표를 입력받고, x, y, z 좌표 각각의 차이를 이용하여 거리를 계산합니다.
모든 행성 쌍에 대해 거리를 계산하면서, 이를 edges 리스트에 저장합니다.

그리고 edges 리스트를 거리를 기준으로 오름차순 정렬합니다.
그 후, 크루스칼 알고리즘을 이용하여 최소 스패닝 트리를 구합니다.
이때, union-find 알고리즘을 이용하여 각 행성이 속한 집합을 구하고, 집합이 같은 경우에는 이를 연결해줍니다.

최소 스패닝 트리의 모든 가중치를 더한 값을 구하고, 이에서 최소 스패닝 트리의 가중치를 빼주면
모든 행성을 연결하는데 드는 최소 비용을 구할 수 있습니다.
'''

import sys

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a < b:
            self.parent[b] = a
        else:
            self.parent[a] = b

n = int(sys.stdin.readline())

# 각 행성들의 좌표를 입력받음
planets = []
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    planets.append((x, y, z, i))

# 각 좌표별로 x, y, z 축을 기준으로 정렬한 간선들을 만듦
edges = []
for j in range(3):
    planets.sort(key=lambda planet: planet[j])
    for i in range(1, n):
        cost = abs(planets[i][j] - planets[i-1][j])
        edges.append((cost, planets[i][3], planets[i-1][3]))

# 간선을 비용 기준으로 정렬
edges.sort()

uf = UnionFind(n)
result = 0
for edge in edges:
    cost, a, b = edge
    if uf.find(a) != uf.find(b):
        uf.union(a, b)
        result += cost

print(result)

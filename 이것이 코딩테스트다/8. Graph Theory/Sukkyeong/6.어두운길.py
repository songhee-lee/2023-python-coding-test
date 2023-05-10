'''
n개의 집과 m개의 도로로 구성
일부 가로등 비활성화하여 최대한 많은 금액을 절약하고자 함
절약할 수 있는 최대 금액을 출력
'''

import sys

# Union-Find 자료구조 클래스
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    # 루트 노드를 찾는 함수
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 두 원소가 속한 집합을 합치는 함수
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a < b:
            self.parent[b] = a
        else:
            self.parent[a] = b

# 입력값 받아오기
n, m = map(int, sys.stdin.readline().split())

edges = []
# 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    edges.append((z, x-1, y-1))

# 간선을 가중치 오름차순으로 정렬
edges.sort()

# Union-Find 객체 생성
uf = UnionFind(n)
result = 0
# 모든 간선에 대해 Union-Find 연산 수행
for edge in edges:
    cost, a, b = edge
    # 두 노드가 같은 집합에 속하지 않으면 연결하고 비용 추가
    if uf.find(a) != uf.find(b):
        uf.union(a, b)
    else:
        result += cost

# 모든 간선의 가중치 합 - 스패닝 트리 간선의 가중치 합
print(sum(edge[0] for edge in edges) - result)

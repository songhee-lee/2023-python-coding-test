''''
마을은 n개의 집과 집들을 연결하는 m개의 길로 이루어짐
마을을 두 개로 분리할 계획
 1. 분리된 두 마을 사이의 길들 없애기
 2. 임의의 두 집 사이의 경로가 존재하므로 길을 더 없앨 수 있음

나머지길의 유지비의 합을 최소로 하고픔

입력을 받습니다.
입력받은 길의 정보를 가중치를 기준으로 오름차순으로 정렬합니다.
초기 상태에서는 모든 집이 각각 하나의 집을 이루고 있습니다. 따라서 각 집을 독립적인 집합으로 나눕니다.
정렬한 길의 정보를 하나씩 탐색합니다.
현재 길의 양 끝점이 속한 집합이 다르면, 이 길을 선택합니다.
선택한 길로 인해 연결된 두 집합을 하나로 합칩니다.
5~6을 모든 길에 대해 반복합니다.
모든 길을 선택한 후, 각 집이 속한 집합 중에서 하나를 선택하여 마을을 나눕니다.
마을을 나눈 후, 마을 안에서의 최소 유지비 합을 구합니다.

'''
import sys

# 특정 원소가 속한 집합을 찾기 위한 함수입니다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치는 함수입니다.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력을 받습니다.
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c, a, b))

# 간선을 가중치를 기준으로 오름차순으로 정렬합니다.
edges.sort()

# 각 집을 독립적인 집합으로 초기화합니다.
parent = [i for i in range(n + 1)]

# 선택한 길로 인해 연결된 두 집합을 하나로 합칩니다.
result = 0
last = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost  # 마지막으로 선택한 간선의 가중치를 저장합니다.

# 마을을 나누기 위해 하나의 집합으로 합칩니다.
# 마지막으로 선택한 간선을 제외합니다.
print(result - last)

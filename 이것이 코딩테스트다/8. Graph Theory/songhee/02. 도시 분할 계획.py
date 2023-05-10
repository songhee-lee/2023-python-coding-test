""" 
- 최소 신장 트리 문제
- MST 2개 만들기 -> 최소 신장 트리 만든 뒤에 가장 비용이 큰 간선 하나 제거하기
"""
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 받기
N, M = map(int, input().split())
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

edges = []          # 간선 정보
result = 0          # 유지비 합
mst = []            # 포함된 간선 비용

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

# 간선 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        mst.append(cost)


print(result - mst[-1])
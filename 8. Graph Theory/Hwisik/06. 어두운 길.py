'''
- 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로 오갈 수 있도록.
- 일부 가로등을 비활성화하여 최대한 많은 금액 절약하기.
-> 크루스칼 알고리즘 사용
'''
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력 받기
n, m = map(int, input().split())

parent = [0] * n # 부모 테이블 초기화
edges = [] # 모든 간선을 담을 리스트
need_cost = 0 # 가로등 활성화 최소 비용
total_cost = 0 # 모든 가로등 활성화 비용

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(n):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    total_cost += cost
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        need_cost += cost

# 절약할 수 있는 최대 금액(모든 가로등 활성화 비용 - 가로등 활성화 최소 비용)
print(total_cost - need_cost)
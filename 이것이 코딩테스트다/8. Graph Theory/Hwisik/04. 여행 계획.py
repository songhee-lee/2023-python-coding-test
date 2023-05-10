'''
- 도로로 연결되어 있다 -> 양방향으로 이동이 가능하다.
- 여행 계획이 가능한지 여부를 판단하라
- 여행 계획이 가능하다는 것은, 여헹 계획에 속한 노드들이 하나의 부분 그래프에 속한다는 의미이다.
- 즉, 여행 계획에 포함된 노드들이 모두 연결되어 있다는 의미이다. -> Union-Find 알고리즘을 이용하면 쉽게 해결할 수 있다.
'''
import sys

input = sys.stdin.readline

# 여행지의 수, 여행 계획에 속한 도시의 수 입력받기
n, m = map(int, input().split())

# 그래프 정보 초기화
graph = []

# 그래프 정보 입력받기
for _ in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

# 여행 계획 입력받기
plans = list(map(int, input().split()))

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 부모 테이블 초기화
parent = [0] * n

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n):
    parent[i] = i

# Union 연산 수행 -> 도로가 연결되어 있는 여행지끼리만 연결
for i in range(n):
    for j in range(n):
        if i != j and graph[i][j] == 1:
            union_parent(parent, i, j)

cannot_travel = False # 여행 계획이 가능한지 여부

# 여행 계획에 속한 노드들이 모두 연결되어 있는지 확인
for i in range(m - 1):
    a, b = plans[i], plans[i + 1]
    # 하나라도 연결되어 있지 않다면
    if find_parent(parent, a) != find_parent(parent, b): 
        cannot_travel = True # 여행이 불가능하다
        break

print('YES' if not cannot_travel else 'NO')
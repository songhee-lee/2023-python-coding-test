'''
- 행성간의 거리를 모두 구하기 -> O(N^2) => 100억으로 시간초과
- 행성간의 거리를 모두 구하지 않고, 행성을 x, y, z축으로 정렬한 후 인접한 행성끼리만 거리를 구함
- 
'''
import sys
input = sys.stdin.readline

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

n = int(input())

parent = [i for i in range(n)] # 부모 테이블 초기화
planets = [] # 행성의 좌표를 저장할 리스트
edges = [] # 간선 정보를 저장할 리스트
ret = 0 # 최소 신장 트리의 비용

for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, i)) # (x, y, z, 임의의 행성 번호)

for i in range(3): # x, y, z 순으로 정렬
    planets.sort(key=lambda x: x[i])
    for j in range(1, n): # 인접한 행성의 좌표 차이를 구함
        edges.append((abs(planets[j][i] - planets[j-1][i]), planets[j][3], planets[j-1][3])) # (거리, 행성 번호, 행성 번호)

edges.sort() # 거리가 짧은 순으로 정렬

# 간선을 하나씩 확인하며
for i in range(len(edges)):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않는 경우에만 집합에 포함
        union_parent(parent, a, b)
        ret += cost

print(ret)
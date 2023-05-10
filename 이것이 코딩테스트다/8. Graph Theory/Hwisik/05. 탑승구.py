'''
- 가능한 큰 번호의 탑승구로 도킹을 한다.
- 도킹 = 탑승구 간 합집합 연산
- 새로운 비행기가 도킹이 되면, 해당 집합을 바로 왼쪽에 있는 집합과 합친다.
- 부모 노드가 0이면, 더 이상 도킹이 불가능하다.
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

# 탑승구의 개수 입력받기
g = int(input())
# 비행기의 개수 입력받기
p = int(input())

parent = [0] * (g + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, g + 1):
    parent[i] = i

docking_cnt = 0 # 도킹한 비행기의 수
for _ in range(p):
    data = find_parent(parent, int(input())) # 현재 비행기의 탑승구의 부모노드 확인
    if data == 0: # 도킹이 불가능한 경우(부모노드가 0인 경우)
        break
    union_parent(parent, data, data - 1) # 도킹이 가능한 경우, 해당 집합과 바로 왼쪽 집합을 합친다.
    docking_cnt += 1

print(docking_cnt)